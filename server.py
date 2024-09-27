import os
from tqdm.auto import tqdm
from datetime import datetime
import discord


from llm import vllm_endpoint
from crawler import crawling
from utils import save_txt, load_txt

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "discord/bot"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    # Your code goes here.



token = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = discord.Client(command_prefix='!',intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} 등장!')


@client.event
async def on_message(message):
    # bot이 스스로 보낸 메시지는 무시
    if message.author == client.user:
        return

    today = datetime.today().strftime('%y%m%d')
    path = os.path.join(os.path.dirname(__file__), 'news', today + '.txt')
    # 해외뉴스 명령어로 뉴스 요약
    if message.content.startswith('해외뉴스'):
        # 오늘의 뉴스가 있으면 보내기
        if os.path.isfile(path):
            response= load_txt(path)
        # 오늘의 뉴스가 없으면 만들기
        else:
            text_list, link_list = crawling()
            response = []

            for text, link in tqdm(zip(text_list, link_list), total = len(text_list), desc = 'generation'):
                response.append(vllm_endpoint(text).rstrip() + '\n' + link)

            save_txt(path, response)

    # LLM 일반 호출 
    else:
        response = [vllm_endpoint(message.content)]

    for r in response:
        await message.channel.send(r)

client.run(token)

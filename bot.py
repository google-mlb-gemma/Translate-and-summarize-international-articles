import os
import discord
from dotenv import load_dotenv
from llm import vllm_endpoint

load_dotenv()

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
    
    response = vllm_endpoint(message.content)
    await message.channel.send(response)

client.run(token)

import os
#from llama_cpp import Llama
from openai import OpenAI


# def llama_endpoint(text: str):
#     model = Llama(
#         model_path='gemma-2-9b-it-Q4_K_M.gguf', #다운로드받은 모델의 위치
#         n_ctx=512,
#         n_gpu_layers= -1        # Number of model layers to offload to GPU
#     )
#     output = model(
#       text, # Prompt
#       max_tokens=512, # Generate up to 32 tokens, set to None to generate up to the end of the context window
#       stop=["<|eot_id|>"], # Stop generating just before the model would generate a new question
#       echo=True # Echo the prompt back in the output
#     )
#     return output['choices'][0]['text'][len(text):]



def vllm_endpoint(text: str, news: bool=True):
    client = OpenAI(
        base_url=os.environ.get("RUNPOD_BASE_URL"),
        api_key=os.environ.get("RUNPOD_API_KEY"),
    )
    if news:
        prompt = f"{text}Read a newspaper article and summarize it in Korean. Write title.Write in 300 characters or less"
    else:
        prompt = text
    response = client.chat.completions.create(
    model="google/gemma-2-9b-it",
    messages=[{"role": "user", "content": prompt}],
    temperature=0,
    # max_tokens=4096,
    )
    # return response.choices[0].message.content
    return response


if __name__ == "__main__":
    print(vllm_endpoint("안녕하세요?"))
from abc import ABC, abstractmethod
import os
import yaml
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
#import sys
#sys.path.append("/data/aisvc_data/NLP/flo/codes/LLM/gemma_sprint/module")
from prompts import *
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_community.chat_models import ChatLlamaCpp

with open("crawl_class.yaml") as f:
    classes = yaml.load_all(f, Loader=yaml.FullLoader)

class Agent(ABC):
    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def summarize(self, content: str) -> str:
        # Implement the logic to summarize the content
        pass


class Gemma(Agent):
    def __init__(self, project_name, model_path, max_tokens=512, n_batch=8192, n_ctx=8192, n_threads=16, temperature=0, verbose=False):
        super().__init__(model_name=model_path)

        self.prompt = PromptTemplate.from_template(SUMMARY_PROMPT)
        
        self.client = ChatLlamaCpp(
            model_path=self.model_name,
            max_tokens=max_tokens,
            n_threads=n_threads,
            n_batch=n_batch,
            n_ctx=n_ctx,
            n_gpu_layers=-1,
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
            verbose=verbose,
            f16_kv=True,
            temperature=temperature,
            top_p=0.9,
            top_k=50
        )

    def summarize(self, article: str):
        chain = self.prompt | self.client | StrOutputParser()
        result = chain.invoke({'article':article})

        return result

    def reflection(self, article: str, ai_result):
        reflection_prompt = PromptTemplate.from_template(REFLECTION_TEST)
        chain = reflection_prompt | self.client | StrOutputParser()
        result = chain.invoke({'article':article, 'ai_result':ai_result})

        return result

    def reflection_batch(self, batch_list: list):
        reflection_prompt = PromptTemplate.from_template(REFLECTION_TEST)
        chain = reflection_prompt | self.client | StrOutputParser()
        result = chain.batch(batch_list)

        return result

    def summarize_chain(self, article: str):
        chain_summarize_prompt = PromptTemplate.from_template(SUMMARY_CHAIN_PROMPT)
        chain = chain_summarize_prompt | self.client | StrOutputParser()
        result = chain.invoke({'article':article})

        return result

    def summarize_chain_batch(self, batch_list: list):
        chain_summarize_prompt = PromptTemplate.from_template(SUMMARY_CHAIN_PROMPT)
        chain = chain_summarize_prompt | self.client | StrOutputParser()
        result = chain.batch(batch_list)

        return result
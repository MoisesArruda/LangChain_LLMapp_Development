import os
import glob
from typing import List
from langchain.chains import LLMChain
from langchain.chat_models import AzureChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma, FAISS
from langchain.document_loaders import PyPDFLoader


from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


def create_chat(t=0.0):
    """
    Configura os objetos do AzureChatOpenAI para serem utilizados.
 
    Args:
        t (float): O valor da temperatura para determinar o comportamento da resposta, por padrão é 0.0.
   
    Returns:
        AzureChatOpenAI: O objeto de AzureChatOpenAi configurado.
    """
    llm_chat = AzureChatOpenAI(openai_api_base=os.getenv("OPENAI_API_BASE"),
                    openai_api_version=os.getenv("OPENAI_API_VERSION"),
                    openai_api_key=os.getenv("OPENAI_API_KEY"),
                    openai_api_type=os.getenv("OPENAI_API_TYPE"),
                    deployment_name=os.getenv("DEPLOYMENT_NAME"),
                    temperature=t
    )
    return llm_chat


def create_embeddings(chunk_size=1):
    embeddings = OpenAIEmbeddings(
        deployment = os.getenv("EMBEDDING_DEPLOYMENT_NAME"),
        chunk_size=chunk_size
    )
    return embeddings


def create_prompt():
    """Cria o prompt a partir do template."""  
    template = """Question: {question}

    Answer: """

    prompt = PromptTemplate(
    template=template,
    input_variables=['question']
    )

def create_chain(prompt,llm):
    
    llm_chain = LLMChain(
        prompt=prompt,
        llm=llm
        )
    
    return llm_chain

#llm=create_chat()

#print(llm.predict("Hello World"))
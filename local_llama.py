from langchain_openai import ChatOpenAI

# super important for chatbot applications
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

##PromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an helpful assistant . Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

st.title('Langchain Demo with Ollama')
input_text = st.text_input("search the topic u want")

##ollama llama3 LLM
llm = Ollama(model="llama2:13b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
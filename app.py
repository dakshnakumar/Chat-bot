from langchain_openai import ChatOpenAI
# super important for chatbot applications
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

##langsmith tracking
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

##PromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are an helpful assistant . Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

##Streamlit framework

st.title("langchain Demo With OPENAI API")
input_text = st.text_input("search the topic u want")

##openAI LLM

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
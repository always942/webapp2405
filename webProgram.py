# 설치 필요
# pip install langchain
import streamlit as st
from langchain_community.llms import OpenAI
import streamlit as st from langchain_community.llms import OpenAI from googlesearch import search from gensim.summarization import summarize

st.title('📰 기사 검색 및 요약 챗봇 📝')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def search_and_summarize(query):
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', '무엇을 도와드릴까요?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('OpenAI API 인증키를 입력해 주세요!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    
    generate_response(text)

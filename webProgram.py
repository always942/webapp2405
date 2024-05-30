# 설치 필요
# pip install langchain
pip install langchain
import streamlit as st from langchain_community.llms import OpenAI from googlesearch import search from gensim.summarization import summarize

st.title('📰 기사 검색 및 요약 챗봇 📝')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def search_and_summarize(query):

기사 검색
results = list(search(query, tld="co.in", num=10, stop=10, pause=2)) st.info('🔍 검색 결과:') for i, result in enumerate(results): st.write(f'{i+1}. {result}')

기사 요약
article = st.selectbox('📝 기사 선택:', results) st.info('📃 기사 요약:') summary = summarize(article) st.write(summary)

AI Chat
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key) st.info(llm(summary))

with st.form('my_form'): text = st.text_input('Enter

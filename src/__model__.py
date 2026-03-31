import streamlit as st
from langchain_community.chat_models import ChatOllama
from .config import MODEL

@st.cache_resource
def get_model():
    return ChatOllama(model=MODEL, temperature=0)

import streamlit as st
from components.ui import badge

def render_home(cfg):
    st.header('Welcome to Tiny AI App')
    st.write('This demo lets you ask questions and summarize text using two model backends.')
    badge('Demo: choose model and interact. Keys loaded from .env')
    st.markdown('---')
    st.write('Quick checks:')
    st.write('- Make sure you have installed the dependencies from requirements.txt')
    st.write('- If a model fails, check your API keys in the Settings page.')

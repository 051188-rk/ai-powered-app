import streamlit as st
from utils.prompt_templates import SUMMARIZE_TEMPLATE

def render_summarizer_ui():
    article = st.text_area('Paste article or URL content here', height=400)
    model = st.selectbox('Choose model', ['groq/openai/gpt-oss-20b', 'gemini'])
    submit = st.button('Summarize (3 sentences)')
    return article, model, submit

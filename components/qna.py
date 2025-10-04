import streamlit as st
from utils.prompt_templates import QNA_TEMPLATE

def render_qna_ui():
    question = st.text_input('Type your question here')
    model = st.selectbox('Choose model', ['groq/openai/gpt-oss-20b', 'gemini'])
    temp = st.slider('Temperature', 0.0, 1.0, 0.7)
    submit = st.button('Ask')
    return question, model, temp, submit

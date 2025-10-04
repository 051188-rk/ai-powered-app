import streamlit as st
from components.qna import render_qna_ui
from utils.groq_client import GroqClient
from utils.gemini_client import GeminiClient
from services.history import add_entry
from services.streamer import stream_response
from models.config import Config
from utils.prompt_templates import QNA_TEMPLATE

def render_qna(cfg):
    st.subheader('Q&A Bot')
    question, model_choice, temp, submit = render_qna_ui()
    cfg = Config.load()
    if submit and question.strip():
        container = st.empty()
        prompt = QNA_TEMPLATE.format(question=question)
        if model_choice.startswith('groq'):
            client = GroqClient(api_key=cfg.get('GROQ_API_KEY'))
            gen = client.chat_stream(model='openai/gpt-oss-20b', messages=[{'role':'user','content':prompt}], temperature=temp)
        else:
            client = GeminiClient(api_key=cfg.get('GEMINI_API_KEY'))
            gen = client.chat_stream(prompt=prompt, temperature=temp)
        full = stream_response(container, gen)
        add_entry('qna', prompt, full)

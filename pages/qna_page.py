import os
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
            # Try to get API key from both environment and config
            groq_api_key = os.getenv('GROQ_API_KEY') or cfg.get('GROQ_API_KEY')
            if not groq_api_key:
                st.error("GROQ_API_KEY not found. Please set it in your .env file.")
                return
            client = GroqClient(api_key=groq_api_key)
            gen = client.chat_stream(model='openai/gpt-oss-20b', messages=[{'role':'user','content':prompt}], temperature=temp)
        else:
            # Try to get API key from both environment and config
            gemini_api_key = os.getenv('GEMINI_API_KEY') or cfg.get('GEMINI_API_KEY')
            if not gemini_api_key:
                st.error("GEMINI_API_KEY not found. Please set it in your .env file.")
                return
            client = GeminiClient(api_key=gemini_api_key)
            gen = client.chat_stream(prompt=prompt, temperature=temp)
        full = stream_response(container, gen)
        add_entry('qna', prompt, full)

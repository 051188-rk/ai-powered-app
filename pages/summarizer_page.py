import streamlit as st
from components.summarizer import render_summarizer_ui
from utils.groq_client import GroqClient
from utils.gemini_client import GeminiClient
from services.history import add_entry
from services.streamer import stream_response
from models.config import Config
from utils.prompt_templates import SUMMARIZE_TEMPLATE

def render_summarizer(cfg):
    st.subheader('3-Sentence Summarizer')
    article, model_choice, submit = render_summarizer_ui()
    cfg = Config.load()
    if submit and article.strip():
        container = st.empty()
        prompt = SUMMARIZE_TEMPLATE.format(article=article)
        if model_choice.startswith('groq'):
            client = GroqClient(api_key=cfg.get('GROQ_API_KEY'))
            gen = client.chat_stream(model='openai/gpt-oss-20b', messages=[{'role':'user','content':prompt}], temperature=0.2)
        else:
            client = GeminiClient(api_key=cfg.get('GEMINI_API_KEY'))
            gen = client.chat_stream(model=cfg.get('GEMINI_MODEL'), prompt=prompt, temperature=0.2)
        full = stream_response(container, gen)
        add_entry('summarize', prompt, full)

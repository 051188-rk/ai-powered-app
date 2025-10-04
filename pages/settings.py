import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

def render_settings(cfg):
    st.subheader('Settings')
    st.write('Environment keys read from your .env')
    st.write({
        'GROQ_API_KEY': bool(cfg.get('GROQ_API_KEY')),
        'GEMINI_API_KEY': bool(cfg.get('GEMINI_API_KEY')),
        'GEMINI_MODEL': cfg.get('GEMINI_MODEL')
    })
    st.markdown('---')
    st.write('If keys are missing, create a `.env` file in the project root with these values:')
    st.code(open('.env.example').read())

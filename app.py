import streamlit as st
from pages.home import render_home
from pages.qna_page import render_qna
from pages.summarizer_page import render_summarizer
from pages.settings import render_settings
from models.config import Config

def main():
    st.set_page_config(page_title="Tiny AI App", layout="wide")
    cfg = Config.load()

    with st.sidebar:
        st.title("Tiny AI App")
        page = st.radio("Choose page", ["Home", "Q&A Bot", "Summarizer", "Settings"])
        st.markdown("---")
        st.caption("Models available: Groq (openai/gpt-oss-20b) and Google Gemini via google.generativeai")
        st.markdown("**Quick tips:** use `.env` for your API keys.")
    if page == "Home":
        render_home(cfg)
    elif page == "Q&A Bot":
        render_qna(cfg)
    elif page == "Summarizer":
        render_summarizer(cfg)
    else:
        render_settings(cfg)

if __name__ == '__main__':
    main()

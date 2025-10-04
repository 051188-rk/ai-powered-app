# Tiny AI App (Streamlit)
This app contains:
- AI Q&A Bot (choose Groq or Gemini)
- Text Summarizer (3-sentence summary)


my first commit: tried implementing gemini client, groq openai/oss with streamlit but failed, tried debugging using gpt but still failed to do so, will try tomorrow morning


Setup:
1. Copy `.env.example` to `.env` and fill keys.
2. Install: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`


Notes:
- Groq client uses `groq` python package pattern (template provided).
- Gemini uses `google.generativeai`. Ensure your environment has access.

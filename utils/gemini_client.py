# Gemini client wrapper using google.generativeai
import os
from dotenv import load_dotenv
load_dotenv()
try:
    import google.generativeai as genai
except Exception:
    genai = None



class GeminiClient:
    def __init__(self, api_key=None):
        self.model = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        if genai is None:
            raise RuntimeError("google.generativeai package not installed.")
        genai.configure(api_key=self.api_key)
        self.genai = genai

    def chat_stream(self, prompt, temperature=0.2):
        # Create a chat session
        chat = self.genai.GenerativeModel(model).start_chat(history=[])
        
        # Get the response with streaming
        response = self.genai.chat.create(model=self.model, messages=[{"role":"user","content":prompt}])

        
        # Stream the response chunks
        for chunk in response:
            if hasattr(chunk, 'text'):
                yield chunk.text

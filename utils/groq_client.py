# Groq client wrapper using the template you provided.
import os
from dotenv import load_dotenv
load_dotenv()
try:
    from groq import Groq
except Exception:
    Groq = None

class GroqClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        if Groq is None:
            raise RuntimeError("groq package not installed or unavailable.")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found. Please set it in your .env file or pass it as an argument.")
        self.client = Groq(api_key=self.api_key)

    def chat_stream(self, model, messages, temperature=1.0, max_tokens=1024):
        # Template streaming code -- yields chunks
        completion = self.client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_completion_tokens=max_tokens,
            top_p=1,
            reasoning_effort="medium",
            stream=True,
            stop=None
        )
        for chunk in completion:
            yield chunk.choices[0].delta.content or ""

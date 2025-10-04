import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    @staticmethod
    def load():
        return {
            'GROQ_API_KEY': os.getenv('GROQ_API_KEY'),
            'GEMINI_API_KEY': os.getenv('GEMINI_API_KEY'),
            'GEMINI_MODEL': os.getenv('GEMINI_MODEL', 'gemini-1.5-mini')
        }

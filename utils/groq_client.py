# Groq client wrapper using the template you provided.
import os
import time
from dotenv import load_dotenv
load_dotenv()

try:
    from groq import Groq
except ImportError:
    Groq = None

class GroqClient:
    def __init__(self, api_key=None):
        # Load API key from environment variable
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables. Please set it in .env file")
            
        if Groq is None:
            raise RuntimeError("groq package not installed. Please install it with: pip install groq")
            
        print(f"Using GROQ API key: {self.api_key[:5]}...{self.api_key[-3:]}")
        
        # Try to initialize the client with retries
        max_retries = 3
        last_error = None
        
        print(f"\n🔍 Debug Info:")
        print(f"- API Key length: {len(self.api_key) if self.api_key else 0}")
        print(f"- API Key starts with: {self.api_key[:5] if self.api_key else 'None'}")
        print(f"- API Key ends with: {self.api_key[-3:] if self.api_key else 'None'}")
        
        for attempt in range(max_retries):
            try:
                print(f"\n🔧 Attempt {attempt + 1} to initialize Groq client...")
                
                # Initialize the client with a timeout
                self.client = Groq(
                    api_key=self.api_key.strip(),  # Ensure we strip any whitespace
                    timeout=30.0,  # 30 seconds timeout
                )
                
                # Test the client with a simple request
                print("Testing API key with models.list()...")
                models = self.client.models.list()
                print(f"✅ Success! Found {len(models.data)} models")
                return  # Success!
                
            except Exception as e:
                last_error = e
                error_msg = str(e).lower()
                print(f"❌ Attempt {attempt + 1} failed: {error_msg}")
                
                if attempt == max_retries - 1:  # Last attempt
                    print("\n🔍 Final error details:")
                    print(f"- Error type: {type(e).__name__}")
                    print(f"- Error message: {str(e)}")
                    
                    if "401" in error_msg or "unauthorized" in error_msg:
                        raise ValueError("❌ Invalid GROQ_API_KEY. The API key was rejected by the server. Please verify your key is correct and has the necessary permissions.")
                    elif "connection" in error_msg or "timeout" in error_msg:
                        raise ConnectionError("🌐 Could not connect to Groq API. Please check your internet connection and try again.")
                    else:
                        raise RuntimeError(f"❌ Failed to initialize Groq client: {str(e)}")
                
                print(f"⚠️ Waiting 1 second before retry...")
                time.sleep(1)  # Wait before retrying

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

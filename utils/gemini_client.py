# Gemini client wrapper using google.generativeai
import os

try:
    import google.generativeai as genai
except Exception:
    genai = None

class GeminiClient:
    def __init__(self, api_key=None, model=None):
        # Load API key and model from environment variables or use provided values
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        self.model = model or os.getenv('GEMINI_MODEL', 'gemini-pro')
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in .env file")
            
        if genai is None:
            raise RuntimeError("google.generativeai package not installed. Install with: pip install google-generativeai")
            
        genai.configure(api_key=self.api_key)
        self.genai = genai
        print(f"Initialized Gemini client with model: {self.model}")

    def chat_stream(self, prompt, temperature=0.2, model=None):
        # Use provided model or fall back to instance model
        model_name = model or self.model
        
        # Create a chat session with the correct model and parameters
        generation_config = {
            'temperature': temperature,
            'max_output_tokens': 2048,
        }
        
        try:
            model = self.genai.GenerativeModel(
                model_name,
                generation_config=generation_config
            )
            chat = model.start_chat(history=[])
            
            # Get the response with streaming
            response = chat.send_message(prompt, stream=True)
            
            # Stream the response chunks
            for chunk in response:
                if hasattr(chunk, 'text'):
                    yield chunk.text
                    
        except Exception as e:
            print(f"Error in chat_stream: {str(e)}")
            yield f"Error: {str(e)}"

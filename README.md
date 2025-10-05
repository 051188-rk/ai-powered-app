# Intern Assignment: Build a Tiny AI-Powered App 

Goal: 
Show us how motivated you are by building a very simple AI-powered app. We don’t care about 
polish or prior coding experience — we care about your effort, resourcefulness, and creativity. 

## ✨ Features

- **AI Q&A Bot** with support for both Groq and Gemini models
- **Text Summarizer** that generates concise 3-sentence summaries
- **Streamlit-based** web interface for easy interaction
- **Environment-based** configuration for API keys

i tried and implemented all of this but i couldnt get it to deploy.

## 🖼️ Screenshots

<div align="center">
  <img src="https://raw.githubusercontent.com/051188-rk/ai-powered-app/main/assets/test1.png" alt="Test Image 1" width="800">
  <img src="https://raw.githubusercontent.com/051188-rk/ai-powered-app/main/assets/test2.png" alt="Test Image 2" width="800">
  <br/>
  <img src="https://raw.githubusercontent.com/051188-rk/ai-powered-app/main/assets/test3.png" alt="Test Image 3" width="800">
  <img src="https://raw.githubusercontent.com/051188-rk/ai-powered-app/main/assets/test4.png" alt="Test Image 4" width="800">
</div>

## 🚀 Quick Start

1. **Setup Environment**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit the .env file with your API keys
   # GEMINI_API_KEY=your_gemini_key_here
   # GROQ_API_KEY=your_groq_key_here
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   streamlit run app.py
   ```

## 📝 Notes

- The application uses environment variables for configuration
- Ensure you have valid API keys for the services you want to use
- The app is configured to work with both Groq and Gemini models

## 🤝 Contributing

Feel free to submit issues and enhancement requests.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

my first commit: tried implementing gemini client, groq openai/oss with streamlit but failed, tried debugging using gpt but still failed to do so, will try tomorrow morning

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("❌ GEMINI_API_KEY not found in .env!")

genai.configure(api_key=api_key)

class GeminiModel:
    def __init__(self):
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text.strip() if response.text else "No response from Gemini."
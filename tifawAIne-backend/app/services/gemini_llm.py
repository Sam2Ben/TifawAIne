"""
Service de gestion du LLM Gemini
"""
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class GeminiLLM:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def generate_response(self, prompt: str) -> str:
        response = await self.model.generate_content(prompt)
        return response.text 
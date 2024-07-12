"""
    Main file, run this file to run project.
"""

from src import API_KEY
from src.model.gemini_AI import GoogleGeminiAI


model = GoogleGeminiAI()
model.configure(API_KEY)
model.set_model('gemini-1.5-flash')
response = model.generate_content("who is spongebob")
print(response)

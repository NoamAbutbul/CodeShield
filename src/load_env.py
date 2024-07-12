"""
    File to load .env file to the system
"""


import os
from dotenv import load_dotenv


load_dotenv("src/configuration/.env")


API_KEY = os.getenv('API_KEY')

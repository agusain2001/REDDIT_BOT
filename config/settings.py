# Project settings for environment configuration
import os
from dotenv import load_dotenv

load_dotenv("config/.env")

class Config:
    REDDIT_CLIENT_ID = os.getenv("CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    REDDIT_USERNAME = os.getenv("USERNAME")
    REDDIT_PASSWORD = os.getenv("PASSWORD")
    REDDIT_USER_AGENT = os.getenv("USER_AGENT")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
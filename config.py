import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bubbly-library-secret-key-2026'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bubbly_library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
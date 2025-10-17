import os

class Config:
    OPENROUTER_KEY = os.environ.get("OPENROUTER_KEY")
    MODEL = os.environ.get("MODEL", "mistralai/mistral-7b-instruct:free")

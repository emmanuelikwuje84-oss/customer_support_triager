import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5")
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./data/support.db",
)

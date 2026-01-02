import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATA_DIR = "data/documents"
VECTOR_DB_DIR = "data/faiss_index"
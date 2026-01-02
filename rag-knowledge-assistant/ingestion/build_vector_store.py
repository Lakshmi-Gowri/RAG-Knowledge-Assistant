from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from config import VECTOR_DB_DIR

def build_vector_store(chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(VECTOR_DB_DIR)

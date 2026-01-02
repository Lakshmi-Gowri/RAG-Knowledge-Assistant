from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from config import VECTOR_DB_DIR

def get_retriever():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(VECTOR_DB_DIR, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever(search_kwargs={"k": 4})

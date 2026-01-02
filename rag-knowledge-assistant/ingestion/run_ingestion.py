from ingestion.load_documents import load_documents
from ingestion.chunk_documents import chunk_documents
from ingestion.build_vector_store import build_vector_store
from config import DATA_DIR

docs = load_documents(DATA_DIR)
chunks = chunk_documents(docs)
build_vector_store(chunks)

print("Ingestion completed successfully.")

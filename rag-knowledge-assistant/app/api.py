from fastapi import FastAPI
from rag.rag_chain import create_rag_chain

app = FastAPI(title="AI Knowledge Assistant")

qa_chain = create_rag_chain()

@app.post("/ask")
def ask_question(query: str):
    response = qa_chain(query)
    return {"answer": response["result"]}

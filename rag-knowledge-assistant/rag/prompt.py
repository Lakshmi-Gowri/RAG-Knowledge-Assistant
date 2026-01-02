from langchain.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an enterprise knowledge assistant.
Answer ONLY using the context provided.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
)

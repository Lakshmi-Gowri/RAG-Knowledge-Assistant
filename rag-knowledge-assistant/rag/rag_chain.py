from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from rag.retriever import get_retriever
from rag.prompt import RAG_PROMPT

def create_rag_chain():
    llm = ChatOpenAI(temperature=0)
    retriever = get_retriever()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": RAG_PROMPT},
        return_source_documents=False
    )

    return qa_chain

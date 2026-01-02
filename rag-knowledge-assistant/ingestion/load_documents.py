import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_documents(data_dir):
    documents = []

    for file in os.listdir(data_dir):
        path = os.path.join(data_dir, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(path)
            documents.extend(loader.load())

        elif file.endswith(".txt"):
            loader = TextLoader(path)
            documents.extend(loader.load())

    return documents

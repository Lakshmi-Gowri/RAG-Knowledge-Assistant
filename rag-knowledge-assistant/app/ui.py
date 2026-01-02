import streamlit as st
import requests

st.set_page_config(page_title="AI Knowledge Assistant")

st.title("📄 AI Knowledge Assistant")

query = st.text_input("Ask a question about your documents")

if st.button("Ask"):
    response = requests.post(
        "http://localhost:8000/ask",
        params={"query": query}
    )
    st.success(response.json()["answer"])

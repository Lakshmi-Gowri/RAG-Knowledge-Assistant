Overview

Retrieval-Augmented Generation app that indexes local docs and serves a QA API + Streamlit UI.

Python 3.10+
Set OpenAI key in .env or environment variable used by config.OPENAI_API_KEY.
Install deps:
pip install -r requirements.txt

python ingestion/run_ingestion.py

Run API
uvicorn app.api:app --reload --host 0.0.0.0 --port 8000

Run Streamlit UI
streamlit run app/ui.py

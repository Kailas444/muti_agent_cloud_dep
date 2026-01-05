from fastapi import FastAPI
from orchestration.graph import app as graph_app

app = FastAPI(title="Multi-Agent RAG System")

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Multi-Agent RAG System is running"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask(query: str):
    result = graph_app.invoke({"query": query})
    return result

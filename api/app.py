from fastapi import FastAPI
from orchestration.graph import app as graph_app

app = FastAPI(title="Multi-Agent RAG System")

# Root endpoint (GET + HEAD)
@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {
        "status": "ok",
        "message": "Multi-Agent RAG System is running"
    }

# Health check (GET + HEAD)
@app.api_route("/health", methods=["GET", "HEAD"])
def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask(query: str):
    result = graph_app.invoke({"query": query})
    return result

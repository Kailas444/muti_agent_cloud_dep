
from fastapi import FastAPI
from orchestration.graph import app as graph_app

api = FastAPI()

@api.post("/ask")
def ask(query: str):
    result = graph_app.invoke({"query": query})
    return result


import gradio as gr
from orchestration.graph import app

def chat(q):
    result = app.invoke({"query": q})
    return result["answer"]

gr.Interface(fn=chat, inputs="text", outputs="text").launch()

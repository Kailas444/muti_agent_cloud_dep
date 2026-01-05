
from langgraph.graph import StateGraph
from typing import TypedDict
from agents.planner_agent import PlannerAgent
from agents.tool_agent import ToolAgent
from agents.rag_agent import RAGAgent
from agents.synthesizer_agent import SynthesizerAgent
import os

class State(TypedDict):
    query: str
    context: str
    answer: str

planner = PlannerAgent()
tool = ToolAgent()
rag = RAGAgent()
synth = SynthesizerAgent(os.getenv("GOOGLE_API_KEY"))

def plan_node(state):
    state["plan"] = planner.plan(state["query"])
    return state

def rag_node(state):
    state["context"] = rag.retrieve(state["query"])
    return state

def synth_node(state):
    state["answer"] = synth.synthesize(state["context"], state["query"])
    return state

graph = StateGraph(State)
graph.add_node("planner", plan_node)
graph.add_node("rag", rag_node)
graph.add_node("synth", synth_node)

graph.set_entry_point("planner")
graph.add_edge("planner", "rag")
graph.add_edge("rag", "synth")
graph.set_finish_point("synth")

app = graph.compile()

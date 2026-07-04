import os

from langgraph.graph import StateGraph, START, END

from ..setttings.saver_config import checkpointer
from ..state import LangGraphState
from ..nodes.claude_code_node import claude_node

graph = StateGraph(LangGraphState)

graph.add_node("call_claude_node",claude_node)
graph.add_edge("call_claude_node", END)
'''
graph.add_node("dispatcher", dispatcher_node)
graph.add_node("exception_route",) # route 적어야 함

graph.add_conditional_edges(
    "exception",
    exception_route,
    {
        "light_weight_llm": "light_weight_llm",
        "heavy_weight_llm": "heavy_weight_llm",
        "end": "dispatcher"
    }
)
'''

app = graph.compile(checkpointer=checkpointer)

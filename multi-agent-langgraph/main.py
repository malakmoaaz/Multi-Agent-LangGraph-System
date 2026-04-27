# main.py
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from state import AgentState
from agents import researcher_node, writer_node, supervisor_node

# 1. Initialize Graph
workflow = StateGraph(AgentState)

# 2. Add Nodes
workflow.add_node("Researcher", researcher_node)
workflow.add_node("Writer", writer_node)
workflow.add_node("Supervisor", supervisor_node)

# 3. Add Edges (The Flow)
workflow.add_edge(START, "Supervisor")
workflow.add_edge("Researcher", "Supervisor")
workflow.add_edge("Writer", "Supervisor")

# 4. Conditional Logic (The Routing)
def router(state: AgentState):
    return state["next"]

workflow.add_conditional_edges(
    "Supervisor",
    router,
    {"Researcher": "Researcher", "Writer": "Writer", "FINISH": END}
)

# 5. Compile and Run
app = workflow.compile()

# Example execution
result = app.invoke({"messages": [HumanMessage(content="Research carbon capture.")]})
print(result)
# At the very bottom of main.py
# Generate a Mermaid URL instead
import base64

mermaid_code = app.get_graph().draw_mermaid()
graphbytes = mermaid_code.encode("ascii")
base64_bytes = base64.b64encode(graphbytes)
base64_string = base64_bytes.decode("ascii")

print(f"View your graph here: https://mermaid.ink/img/{base64_string}")
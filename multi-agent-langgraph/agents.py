# agents.py
from state import AgentState
from langchain_core.messages import HumanMessage

def researcher_node(state: AgentState):
    print("--- RESEARCHER WORKING ---")
    # In a real app, you'd call a search tool here
    return {"messages": [HumanMessage(content="I found some data on carbon capture: it uses DAC and amine scrubbing.")]}

def writer_node(state: AgentState):
    print("--- WRITER WORKING ---")
    # In a real app, you'd use an LLM to format the researcher's notes
    return {"messages": [HumanMessage(content="SUMMARY: Carbon capture is a tech that filters CO2 from the air using DAC.")]}

def supervisor_node(state: AgentState) -> dict:
    print("--- SUPERVISOR ROUTING ---")
    last_message = state["messages"][-1].content
    
    # 1. If it's the very start, send to Researcher
    if "Research" in last_message:
        return {"next": "Researcher"}
    
    # 2. If the Researcher just finished (we see "data"), send to Writer
    if "data" in last_message.lower():
        return {"next": "Writer"}
    
    # 3. Otherwise, we are done
    return {"next": "FINISH"}
# state.py
from typing import Annotated, Sequence, TypedDict
import operator
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    # The 'messages' key accumulates conversation history via operator.add
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' key tracks which agent should act next
    next: str
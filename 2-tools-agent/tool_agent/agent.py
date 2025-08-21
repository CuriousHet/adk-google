from google.adk.agents import Agent
from google.adk.tools import google_search  # built-in tool
from datetime import datetime 

# functional tool 
def get_current_time() -> dict:
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    """,
    # tools=[google_search], # can use only 1 tool at a time i.e. can't pass multiple tool at a time 
    tools=[get_current_time], 
    # tools=[google_search, get_current_time], # Doesn't work
)  
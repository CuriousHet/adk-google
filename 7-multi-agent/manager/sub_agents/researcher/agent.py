from google.adk.agents import Agent
from google.adk.tools import google_search # <-- Import the built-in tool

researcher_agent = Agent(
    name="researcher",
    model="gemini-2.0-flash",
    description="A specialized agent for conducting research on a given topic.",
    instruction="""
    You are a research assistant. Your task is to use the provided google_search tool
    to find relevant information on the given topic and provide a summary of your findings.
    """,
    tools=[google_search], 
)
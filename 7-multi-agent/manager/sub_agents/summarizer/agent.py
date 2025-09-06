from google.adk.agents import Agent

summarizer_agent = Agent(
    name="summarizer",
    model="gemini-2.0-flash",
    description="A specialized agent that summarizes a given text.",
    instruction="""
    You are a summarization expert. Your sole purpose is to take the input text from writer agent
    and provide a concise summary.
    """,
)
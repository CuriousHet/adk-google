from google.adk.agents import Agent

writer_agent = Agent(
    name="writer",
    model="gemini-2.0-flash",
    description="A specialized agent for writing articles based on provided research.",
    instruction="""
    You are a content writer. Your task is to write engaging article
    based on the research material provided to you and pass it summarizer agent for generating summary.
    """,
)
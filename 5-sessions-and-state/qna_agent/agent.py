from google.adk.agents import Agent

qna_agent = Agent(
    name="qna_agent",
    model="gemini-2.0-flash",
    description="An agent that answers questions",
    instruction="""
    You are a helpful assistant that answers questions based on provided context.

    Here is some information about user:
    Name:
    {user_name}
    Preferences:
    {user_preferences}
    """,
)
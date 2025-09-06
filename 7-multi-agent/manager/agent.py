from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.researcher.agent import researcher_agent
from .sub_agents.writer.agent import writer_agent
from .sub_agents.summarizer.agent import summarizer_agent

# Designate the root agent for the ADK to discover.
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="The manager of the content creation team.",
    instruction="""
    You are the manager of a content creation team. Your job is to oversee the
    process of creating an article on a user-specified topic.

    Follow these steps:
    1. Delegate the research to the 'researcher' tool.
    2. Pass the research findings to the 'writer' agent to create the article.
    3. Once the article is written, use the 'summarizer' agent to create a summary.
    4. Present the final article and the summary to the user.

    You are responsible for delegating tasks to the following agents:
    - writer
    - summarizer

    You also have access to the following tools:
    - researcher
    """,
    sub_agents=[writer_agent, summarizer_agent],
    tools=[
        AgentTool(researcher_agent),
    ],
)
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.planner.agent import planner_agent
from .sub_agents.booking.agent import booking_agent
from .sub_agents.notifier.agent import notifier_agent

# Designate the root agent for the ADK to discover.
root_agent = Agent(
    name="manager",
    model="gemini-2.0-flash",
    description="The manager of the travel booking team.",
    instruction="""
    You are the manager of a travel booking team. Your job is to oversee the
    process of planning and booking a trip for a user.

    Follow these steps:
    1. Delegate the travel planning to the 'planner' agent.
    2. Pass the created travel plan to the 'booking' agent to make the reservations.
    3. Once the booking is confirmed, use the 'notifier' agent to send the details to the user.
    4. Present the final booking confirmation and notification status to the user.
    5. Throughout the process, update the session state with the trip details,
       booking confirmation, and notification status.

    You are responsible for delegating tasks to the following agents:
    - planner
    - booking
    - notifier
    """,
    sub_agents=[planner_agent, booking_agent, notifier_agent],
)
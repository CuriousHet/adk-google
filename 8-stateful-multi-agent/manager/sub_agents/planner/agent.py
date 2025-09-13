from google.adk.agents import Agent

planner_agent = Agent(
    name="planner",
    model="gemini-2.0-flash",
    description="The travel planner specialist.",
    instruction="""
    You are a travel planner. Your task is to take a user's travel request
    and create a detailed itinerary.

    The itinerary should include:
    - Destination
    - Travel dates
    - Suggested flights
    - Accommodation options
    - A brief list of activities.

    Once you have created the plan, return it to the manager.
    """,
)
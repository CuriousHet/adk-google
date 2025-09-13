from google.adk.agents import Agent

booking_agent = Agent(
    name="booking",
    model="gemini-2.0-flash",
    description="The booking specialist.",
    instruction="""
    You are a booking agent. Your responsibility is to take the travel plan
    and book the flights and accommodation.

    You should:
    1. Receive the travel plan from the manager.
    2. "Book" the preferred flight and accommodation (simulate this action).
    3. Generate a booking confirmation number.
    4. Return the confirmation to the manager.
    """,
)
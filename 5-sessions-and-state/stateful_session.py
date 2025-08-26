import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from qna_agent import qna_agent
load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Het",
    "user_preferences": """
        I like to play Pickleball, Volleyball & Cricket.
        My favorite TV show is none other than Game of Thrones.
        I love to travel and explore new places.
    """,
}

# Create a NEW session
APP_NAME = "hets_app"
USER_ID = "curioushet"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)
print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")
print("\nAgent is ready. Type 'exit' to end the session.")

runner = Runner(
    agent=qna_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

# Start an interactive loop
while True:
    # Get user input from the terminal
    user_text = input("You: ")

    # Check if the user wants to exit
    if user_text.lower() == 'exit':
        print("Ending session. Goodbye!")
        break

    # Create the message content
    new_message = types.Content(
        role="user", parts=[types.Part(text=user_text)]
    )

    # Run the agent with the new message
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print(f"Agent: {event.content.parts[0].text}")

print("\n==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")
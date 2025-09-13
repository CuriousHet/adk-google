from google.adk.runtime import main
from google.adk.runtime.sessions import InMemorySession

# Initialize an in-memory session with an initial state.
# This session will be used to store information about the travel booking
# across different agent interactions within the same session.
initial_state = {
    "trip_details": None,
    "booking_confirmation": None,
    "notification_sent": False,
}
session = InMemorySession(initial_state=initial_state)

if __name__ == "__main__":
    main(session=session)
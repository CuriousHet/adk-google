from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject of the email, should be precise and valid"
    )
    body: str = Field(
        description="The body content of the email, should be clear and concise and well-structured with proper greetings and sign-off"
    )

root_agent = LlmAgent(

    name="email_agent",
    model="gemini-2.0-flash",
    instruction="""

    You are an expert email writer.
    
    GUIDELINES:
    - Ensure the subject is relevant and concise.
    - The body should be well-structured with a clear introduction, main content, and conclusion.
    - Use proper greetings and sign-off.
    - Maintain a professional and polite tone.
    - Avoid unnecessary jargon and be clear and to the point.

    IMPORTANT:
    - Always respond in the JSON format as specified below.
    {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
    }

    DO NOT include any explanations or additional text outside the JSON structure.
    """,
    description="An agent that generates well-structured email content based on user prompts.",
    output_schema=EmailContent,
    output_key="email"
)
import os
import random
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Hugging Face OpenAI-compatible endpoint (needs HF token in env)
#   export HF_TOKEN="hf_xxxxxxxxx"
model = LiteLlm(
    model="openai/HuggingFaceTB/SmolLM3-3B:hf-inference",
    api_base="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN"),
)

# --- Tools ---

def ai_trend(**kwargs):
    trends = [
        "Edge AI is shifting computation from cloud to on-device models for privacy and speed.",
        "Generative AI is being integrated into developer IDEs for real-time code assistance.",
        "Multi-modal models that combine vision, text, and audio are rapidly evolving.",
        "Open-weight LLMs are gaining traction as enterprises push for transparency and cost control.",
    ]
    return random.choice(trends)

def coding_best_practice(**kwargs):
    practices = [
        "Write tests before adding new features; it forces clarity in design.",
        "Keep functions pure when possible: input in, output out, no hidden state.",
        "Name variables for meaning, not mechanics—`user_id` > `uid`.",
        "Use version control branches for each feature; avoid long-lived unmerged branches.",
    ]
    return random.choice(practices)

def historic_ai_fact(**kwargs):
    facts = [
        "In 1956, the Dartmouth Conference coined the term 'Artificial Intelligence'.",
        "The first chatbot, ELIZA, was built in 1966 by Joseph Weizenbaum.",
        "Backpropagation, crucial for training neural nets, became popular in the 1980s.",
        "AlphaGo’s 2016 victory over Lee Sedol marked a turning point for deep learning in games.",
    ]
    return random.choice(facts)

# --- Agent ---

root_agent = Agent(
    name="tech_agent",
    model=model,
    description="Agent that provides AI/tech insights, practices, and history",
    instruction="""
    You are a technology insights assistant.
    You never reply with plain text answers.
    Always respond by invoking one of the tools: `ai_trend`, `coding_best_practice`, or `historic_ai_fact`.
    """,
    tools=[ai_trend, coding_best_practice, historic_ai_fact],
)

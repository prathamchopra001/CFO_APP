from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = LLM(
    provider="ollama",
    model="llama3.1:8b ",
    verbose=True,
    base_url="http://localhost:11434"
)



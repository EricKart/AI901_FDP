"""
Lab 2 — Lightweight chat client with the Foundry SDK (Azure OpenAI).
Fill .env first (see .env.example), then:  python chat_client.py
Exam objective: create a lightweight chat client with the Foundry SDK.
"""
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
)

DEPLOYMENT = os.getenv("CHAT_DEPLOYMENT", "gpt-4o-mini")

# --- Try editing the SYSTEM message and the parameters, then re-run ---
SYSTEM = "You are a concise, encouraging AI-901 study coach."

messages = [
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": "Give me three quick tips to beat exam nerves."},
]

resp = client.chat.completions.create(
    model=DEPLOYMENT,          # <-- the DEPLOYMENT name, not the base model
    messages=messages,
    temperature=0.7,           # randomness (lower = more focused)
    max_tokens=300,            # response LENGTH cap
)

print("\n--- Assistant reply ---")
print(resp.choices[0].message.content)   # the generated text lives here
print("\n(tokens used:", resp.usage.total_tokens, ")")

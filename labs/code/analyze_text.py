"""
Text-analysis mini-lab — prompt a model to return structured analysis as JSON.
Exam objective: build a lightweight application that includes text analysis.
Run:  python analyze_text.py
"""
import os, json
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
client = AzureOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
)
DEPLOYMENT = os.getenv("CHAT_DEPLOYMENT", "gpt-4o-mini")

SYSTEM = (
    "You are a text-analysis tool. For the user's text return ONLY JSON with keys: "
    "sentiment (positive|negative|neutral|mixed), key_phrases (array), "
    "entities (array of {text, category}), summary (one sentence)."
)

texts = [
    "The room was spotless and the staff were lovely, but check-in took forever.",
    "Battery life is incredible; however the camera is disappointing in low light.",
]

for t in texts:
    resp = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": t}],
        temperature=0,          # deterministic output for analysis
        response_format={"type": "json_object"},
    )
    print("\nINPUT:", t)
    try:
        print(json.dumps(json.loads(resp.choices[0].message.content), indent=2))
    except Exception:
        print(resp.choices[0].message.content)

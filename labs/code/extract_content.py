"""
Lab 4 (template) — Extract structured info with Azure Content Understanding.
Exam objective: extract information from documents/images/audio/video with
Azure Content Understanding in Foundry Tools.

The Content Understanding API/SDK is evolving; this is a TEMPLATE showing the
shape (create analyzer with a field schema -> analyze a file -> read JSON).
Do the portal version in Lab 4; use this to see the code pattern.
"""
import os, time, requests
from dotenv import load_dotenv

load_dotenv()

# From your Content Understanding resource / Foundry Tools:
ENDPOINT = os.getenv("CONTENT_UNDERSTANDING_ENDPOINT", "https://YOUR-RESOURCE.cognitiveservices.azure.com")
KEY = os.getenv("CONTENT_UNDERSTANDING_KEY", "YOUR_KEY")
API_VERSION = "2024-12-01-preview"

# 1) A field schema = the fields you want extracted (this drives everything).
analyzer_definition = {
    "description": "Invoice fields for AI-901 demo",
    "fieldSchema": {
        "fields": {
            "vendor":       {"type": "string"},
            "invoice_date": {"type": "date"},
            "total":        {"type": "number"},
        }
    },
}

HEADERS = {"Ocp-Apim-Subscription-Key": KEY, "Content-Type": "application/json"}


def analyze(file_url):
    """Illustrative call flow: submit -> poll -> read structured result."""
    submit = requests.post(
        f"{ENDPOINT}/contentunderstanding/analyzers/invoice-demo:analyze",
        params={"api-version": API_VERSION},
        headers=HEADERS, json={"url": file_url},
    )
    submit.raise_for_status()
    op_url = submit.headers.get("operation-location")
    while True:
        r = requests.get(op_url, headers={"Ocp-Apim-Subscription-Key": KEY}).json()
        if r.get("status") in ("succeeded", "failed"):
            return r
        time.sleep(2)


if __name__ == "__main__":
    print("This is a template. Complete Lab 4 in the Foundry portal first,")
    print("then plug your endpoint/key/analyzer id here to run programmatically.")
    print("Field schema to extract:", list(analyzer_definition["fieldSchema"]["fields"]))

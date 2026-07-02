# Module 04 — Text Analysis & NLP
### Day 4 · Session 1 | Domain 1 (text-analysis techniques) + Domain 2 (implement text apps in Foundry)

AI-901 names four text-analysis techniques explicitly: **keyword extraction, entity detection, sentiment analysis, and summarization.** You must recognize each, and be able to **implement a lightweight text-analysis app in Foundry** (either by prompting a model or using text tools).

---

## PART 0 — How NLP works (concept units: tokenization → statistical → semantic)

The official concepts module builds NLP up in three layers — recognize each:
- **Tokenization** — split text into **tokens** (word-pieces) so a model can process it. Foundational to *both* classic NLP and LLMs. (Same "token" idea as Module 02.)
- **Statistical text analysis** — older techniques based on **word frequency/counts** (e.g., bag-of-words, TF-IDF, frequency of terms). Good for keyword extraction and simple classification; **doesn't truly understand meaning**.
- **Semantic language models** — modern approach using **embeddings** and **transformers** to capture **meaning/context** (so "car" ≈ "automobile"). Powers today's sentiment, entities, summarization, and generative NLP.

> **Exam cue:** *"counts word frequencies / bag-of-words"* → **statistical**. *"captures meaning so synonyms match / context-aware"* → **semantic (embeddings + transformers)**.

---

## PART A — Text-analysis techniques (Domain 1) ⭐ know these four cold

| Technique | What it returns | Example | Exam cue |
|---|---|---|---|
| **Keyword / key-phrase extraction** | The main talking points/terms | "The hotel room was clean and spacious" → *hotel room, clean, spacious* | *"pull the main topics/terms"* |
| **Entity detection (NER)** | Named entities by category: Person, Location, Organization, DateTime, Quantity… | "Satya Nadella visited Paris in 2024" → Person, Location, DateTime | *"identify people/places/orgs/dates"* |
| **Sentiment analysis** | Positive / Negative / Neutral / Mixed (+ scores) | "Great food but slow service" → **Mixed** | *"is the opinion positive or negative?"* |
| **Summarization** | A shorter version (extractive or abstractive) of long text | Condense a document/conversation | *"produce a concise summary"* |

### Related NLP capabilities to recognize
- **Language detection** — identify the language of text.
- **PII detection** — find/redact personal info (names, emails, phone, IDs).
- **Entity linking** — disambiguate an entity to a knowledge base (e.g., which "Mars").
- **Translation** — convert text between languages (Azure AI Translator concept).
- **Conversational Language Understanding (CLU)** — extract **intent + entities** from an utterance (e.g., "book a room" → intent `BookRoom`). *Replaces legacy LUIS.*
- **Question answering** — return answers from an FAQ knowledge base. *Replaces legacy QnA Maker.*

> **Exam traps:**
> - *"positive or negative?"* → **sentiment** (not key phrases).
> - *"pull the main topics"* → **keyword extraction** (not sentiment).
> - *"find & remove emails/phone numbers"* → **PII detection**.
> - *"figure out what the user wants to do (their intent)"* → **CLU**.
> - *"answer 'what are your opening hours?' from a help page"* → **question answering** (not CLU).

---

## PART B — Implementing text analysis in Foundry (Domain 2)

The exam objective: *"Build a lightweight application that includes text analysis."* In AI-901 there are **two valid approaches** — know both:

### Approach 1 — Prompt a deployed model to do the analysis
A general chat/multimodal model can do sentiment, extraction, and summarization if you instruct it well. The **system prompt** defines the task and output shape:

```python
from openai import AzureOpenAI
client = AzureOpenAI(azure_endpoint=ENDPOINT, api_key=KEY, api_version="2024-10-21")

review = "The room was spotless but check-in took forever."
resp = client.chat.completions.create(
    model="gpt-4o-mini",  # your deployment
    messages=[
        {"role": "system", "content":
         "You are a text-analysis tool. For the user's text, return JSON with "
         "keys: sentiment (positive/negative/neutral/mixed), key_phrases (list), "
         "entities (list), summary (one sentence)."},
        {"role": "user", "content": review},
    ],
    temperature=0,           # deterministic for analysis tasks
)
print(resp.choices[0].message.content)
```
Teaching point: **low temperature** for analytical/extraction tasks; **structured output** via a clear system prompt.

### Approach 2 — Use a purpose-built text/Language capability
For classic NLP at scale you can call a dedicated text-analysis capability (the Azure AI **Language** service / its features) that returns sentiment, key phrases, entities, PII, and summaries directly — no prompt engineering, consistent structured results. Choose this when you want **deterministic, pre-built** analytics rather than a generative model's interpretation.

> **Exam angle — when to use which:** A **model + prompt** is flexible and multilingual but less deterministic; a **prebuilt Language capability** gives consistent, structured results for standard tasks. Fundamentals questions may ask you to pick based on "consistent structured output" vs "flexible reasoning."

---

## C. Session 1 live-demo checklist
1. **Foundry playground**: paste 3 reviews; system-prompt the model to output sentiment + key phrases + summary as JSON. Show the **Mixed** case.
2. Change **temperature** 0 → 1; show why 0 is better for analysis.
3. Show entity + PII extraction by prompt; discuss redaction.
4. Contrast with a prebuilt Language capability's structured JSON (concept).

## D. Scenario drill
| Scenario | Answer |
|---|---|
| Score reviews positive/negative | **Sentiment analysis** |
| Pull the main topics from articles | **Keyword extraction** |
| Extract Person/Org/Location/Date | **Entity detection (NER)** |
| Redact emails & phone numbers | **PII detection** |
| Condense a long report to 3 lines | **Summarization** |
| Detect a user's intent "cancel my booking" | **CLU (intent + entities)** |
| Answer FAQ questions from a help doc | **Question answering** |
| Translate text into 10 languages | **Translation (Translator)** |

## E. Rapid recall
1. Four named text-analysis techniques in AI-901? *(keyword extraction, entity detection, sentiment, summarization)*
2. Best temperature for extraction tasks? *(0 / low)*
3. Legacy names replaced by CLU and question answering? *(LUIS; QnA Maker)*
4. "Find and remove SSNs" = which capability? *(PII detection)*
5. Model+prompt vs prebuilt Language — which gives consistent structured output? *(prebuilt Language capability)*

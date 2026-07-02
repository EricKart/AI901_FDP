# Module 01 — Responsible AI & AI Workloads
### Day 3 · Session 1 | Exam Domain 1: "Identify AI concepts and capabilities" (40–45%)

This module covers two sub-skills of Domain 1: **principles of responsible AI** and **identifying AI workloads**. (The third sub-skill, *how gen-AI models work & model config*, is Module 02.)

---

## PART A — Responsible AI: Microsoft's SIX principles ⭐ (guaranteed marks)

Unchanged from AI-900 — but AI-901 asks you to *describe considerations* for each in a solution context. Memorize all six + a one-line consideration + example. Mnemonic **"F.R.I.T.A.P."**: **F**airness, **R**eliability & safety, **I**nclusiveness, **T**ransparency, **A**ccountability, **P**rivacy & security.

| # | Principle | Consideration (what to do) | Example | Classic exam trap |
|---|---|---|---|---|
| 1 | **Fairness** | Treat everyone equitably; detect & mitigate **bias** in data/outputs | A loan model must not disadvantage a gender/ethnicity | *"Different results by ethnicity / demographic"* → Fairness |
| 2 | **Reliability & Safety** | Perform **consistently** and safely, incl. under unexpected conditions; rigorous testing | Self-driving car behaves safely in fog | *"Works consistently / rigorous testing / handles new situations"* → Reliability & safety |
| 3 | **Privacy & Security** | Protect personal data; consent; secure the system & model | De-identify training data; guard against attacks | *"Protect personal/consumer data"* → Privacy & security |
| 4 | **Inclusiveness** | Empower **everyone**, all abilities & backgrounds | Captions for deaf users; works across languages/regions | *"Accessible to people with disabilities"* → Inclusiveness |
| 5 | **Transparency** | People understand **how it works and its limits**; disclose it's AI | Tell users it's AI; explain data used and why | *"Users understand behaviour & limitations"* → Transparency |
| 6 | **Accountability** | **People/orgs are answerable**; governance, compliance, oversight | A governance board owns outcomes & meets law/ethics | *"People remain responsible / governance framework / oversight board"* → Accountability |

> **The two everyone confuses:**
> - **Reliability & Safety** = the *system* behaves correctly/safely.
> - **Accountability** = *people/organizations* are answerable and set up governance.
> Test: *"An oversight board reviews the AI's decisions and answers for them."* → **Accountability**.

### Responsible AI for **generative** AI (new emphasis in AI-901)
Because the exam centres on gen-AI, expect responsible-AI questions framed around LLMs:
- **Content Safety** — filter/moderate **harmful content** (hate, violence, self-harm, sexual) in prompts and responses. Configurable severity thresholds. (In Foundry, deployments have content filters.)
- **Grounding / RAG** to reduce **hallucinations** (making up facts) → supports reliability & transparency.
- **Prompt shields / jailbreak protection** — defend against prompt-injection attacks → security.
- **Transparency notes / system messages** disclosing the AI's role and limits.
- **Human oversight** ("human in the loop") for high-impact decisions → accountability.

---

## PART B — AI workloads (recognize the scenario → name the workload)

AI-901 explicitly lists these workload categories. Learn to spot each from a one-line scenario.

| Workload | What it does | Everyday scenario | Where you build it (AI-901) |
|---|---|---|---|
| **Generative AI** | *Creates* new content (text, images, code) | Draft an email, summarize a report, generate an image | Deploy a model in **Foundry**; prompt it |
| **Agentic AI** | An AI **agent** that reasons + **uses tools/knowledge to act** | "Book the meeting and email attendees" | **Foundry Agent Service** |
| **Text analysis (NLP)** | Understand written language | Sentiment of reviews, extract entities, summarize | Multimodal/text model or text tools in **Foundry** (Module 04) |
| **Speech** | Recognize & synthesize spoken language | Transcribe a call; read text aloud | **Azure Speech in Foundry Tools** (Module 05) |
| **Computer vision** | Interpret images/video | Describe a photo, read text in an image | **Multimodal model** in Foundry (Module 03) |
| **Image generation** | *Create* images from text | Generate a product mock-up | **Image model** (DALL·E / GPT-image) in Foundry (Module 03) |
| **Information extraction** | Pull **structured info** from documents, images, audio, video | Extract invoice fields; summarize a video | **Azure Content Understanding** (Module 05) |
| **Machine learning (classic)** | Predict values/categories from data | Predict churn, forecast sales | Azure Machine Learning (light coverage) |

> **Exam framing:** They give a scenario, you pick the workload/capability. *"An app that describes photos aloud for blind users"* → computer vision (image description via a **multimodal model**) + **speech synthesis** (text-to-speech).

### Core capabilities vocabulary (recognize these terms)
- **Prediction/regression** → a number. **Classification** → a category. **Clustering** → grouping unlabeled data. **Anomaly detection** → outliers.
- **Computer vision** → image/video understanding. **NLP** → language understanding/generation. **Speech** → spoken language.
- **Knowledge mining / information extraction** → surfacing structured info from unstructured content.
- **Generative AI** → producing novel content. **Agentic AI** → autonomous, tool-using AI.

### Considerations & challenges of AI solutions
- **Bias** (biased data → unfair results), **errors causing harm**, **data privacy/security**, **trust/transparency**, **explainability** ("black box"), **hallucination** in gen-AI. These motivate the responsible-AI principles above.

---

## C. Session 1 live-demo checklist
1. Whiteboard **F.R.I.T.A.P.**; run 4 rapid scenario calls with the group.
2. Open the **Foundry portal (ai.azure.com)** → show the **model catalog** and a chat **playground** (sets up everything to come).
3. Show a deployment's **content filter** settings → ties responsible AI to a real control.
4. Map 5 everyday scenarios to workloads out loud.

## D. Rapid recall (ask verbally)
1. Name the six principles. *(F,R,I,T,A,P)*
2. A model denies more loans to one ethnic group → which principle? *(Fairness)*
3. "The AI tells users it's an AI and states its limits" → ? *(Transparency)*
4. An oversight board answers for the AI's decisions → ? *(Accountability)*
5. Filtering hate/violence in LLM output uses…? *(Content Safety / content filters)*
6. "Book a flight and email the itinerary" — plain chat or an **agent**? *(Agent — it uses tools to act)*
7. Extract totals from scanned invoices → which workload/service? *(Information extraction → Content Understanding)*
8. Generate an image from a text description → ? *(Image generation model)*

# Module 06 — Microsoft Foundry: Portal, Model Catalog & Deployment
### Day 3 S1 orientation → Day 5 | Exam Domain 2: "Implement AI solutions by using Microsoft Foundry" (55–60%)

Foundry is the centre of gravity for AI-901. Everything — models, playgrounds, agents, tools, content safety, evaluations — lives here. This module covers **the portal and deploying/interacting with a model**; Module 07 covers the **SDK and agents**.

---

## A. What Microsoft Foundry is

**Microsoft Foundry** (formerly **Azure AI Foundry**, formerly **Azure AI Studio**) is the unified platform to **build, deploy, evaluate, and manage** AI apps and agents. Access it at **`ai.azure.com`** (the **Foundry portal**), or from code with the **Foundry SDK**.

### Structure / key objects (recognize these)
| Object | What it is |
|---|---|
| **Hub** | Top-level collaborative workspace: shared security, connections, compute, resources |
| **Project** | A workspace inside a hub where you build a specific solution (deployments, agents, files, evaluations) |
| **Model catalog** | Browse/deploy thousands of models: Azure OpenAI (GPT-4o, o-series, DALL·E, embeddings), Microsoft **Phi**, Meta **Llama**, **Mistral**, **Cohere**, etc. |
| **Deployments** | A model you've made callable (with a **deployment name**, endpoint, quota, content filter) |
| **Playground** | In-browser chat/assistants/images/real-time to test prompts and models — **no code** |
| **Tools** | Built-in capabilities: **Azure Speech**, **Content Understanding**, search/grounding, function tools |
| **Agents** | Agent Service to create model+instructions+tools agents (Module 07) |
| **Connections** | Links to data/resources (e.g., Azure AI Search, Storage) for grounding/RAG |
| **Evaluations** | Test model/app quality (groundedness, relevance, safety) |
| **Content filters / Content Safety** | Responsible-AI guardrails on each deployment |

---

## B. Deploy a model and interact with it in the portal (exam objective)

**Steps (teach this as a live demo):**
1. **Foundry portal → your project → Model catalog.** Search a model (e.g., **GPT-4o-mini**).
2. Click **Deploy** → choose a **deployment type** (Standard / Global Standard / Provisioned / Serverless — see Module 02) → name it (this **deployment name** is what code references).
3. Review the **content filter** (default responsible-AI guardrails).
4. Open the **Chat playground** → select the deployment → set the **system message** → send **user** prompts.
5. Adjust **parameters** (temperature, max tokens, top_p) and observe behaviour.
6. Use **"View code"** to get a ready-made SDK/REST snippet (bridge to Module 07).

> **Exam cues:** the thing you reference in code is the **deployment name** (not the base model name). The **endpoint + key** (or **Microsoft Entra ID**) authenticate calls. The **system message** steers behaviour before any user prompt.

### Using Microsoft Foundry **endpoints** (official unit — know this)
Once deployed, a model/app is reached through an **endpoint** — a URL your code (or REST call) targets. Recognize:
- **Project / Foundry endpoint** — connect via the **Foundry SDK** (`AIProjectClient`) to reach the project's deployments, agents, and tools.
- **Azure OpenAI endpoint** — `https://<resource>.openai.azure.com/`, used by the `AzureOpenAI` client.
- **Model inference endpoint** — a unified endpoint for calling many catalog models via `azure-ai-inference`.
- Every endpoint call needs **auth** (API **key** or **Microsoft Entra ID**) + the **deployment name** + an **API version**.

> **Exam cue:** "what does the app connect to in order to call the model?" → the **endpoint** (plus key/Entra + deployment name).

---

## C. Prompt engineering in the playground (system vs user prompts) ⭐

A chat request is a list of **messages**; the exam tests the **roles**:

| Role | Purpose | Example |
|---|---|---|
| **system** | Persona, rules, format, grounding, guardrails — set **before** the conversation | "You are a concise travel assistant. Only answer using the provided policy text. Refuse off-topic requests." |
| **user** | The actual request | "Suggest a 3-day Goa itinerary." |
| **assistant** | The model's prior replies (kept for context) | (previous answers) |

### Prompt-engineering techniques to teach
- **Clear, specific instructions** — state task, format, constraints.
- **Few-shot examples** — show 1–3 input→output examples to shape responses.
- **Grounding** — paste/inject the source data the model must use (reduces hallucination).
- **Output format control** — "return JSON with keys …".
- **Chain-of-thought / step-by-step** — ask the model to reason for complex tasks.
- **Guardrails in the system prompt** — refusals, scope limits, tone.

> **Exam trap — where do rules go?** Persona/rules/grounding/format constraints belong in the **system** message; the specific request goes in the **user** message. A distractor will try to put rules in the user prompt.

---

## D. Grounding / RAG (concept the exam expects)
- **Grounding** = give the model your **authoritative data** so answers are fact-based.
- **RAG (Retrieval-Augmented Generation)** = retrieve relevant chunks (often via **Azure AI Search** + **embeddings**) and add them to the prompt at query time.
- In Foundry you **connect a data source** (e.g., "Add your data" / Azure AI Search) to ground a chat.
- Benefits: fewer **hallucinations**, answers cite **your** content, no retraining needed.

---

## E. Content Safety & evaluation (Responsible AI in Foundry)
- Every deployment has **content filters** (hate, violence, sexual, self-harm) with adjustable **severity thresholds**; plus **prompt shields** (jailbreak/prompt-injection defense) and **groundedness/protected-material** detection.
- **Evaluations** measure app quality: **groundedness, relevance, coherence, fluency, safety** — run against test data before shipping.

---

## F. Day-3 orientation demo checklist
1. Tour the **Foundry portal**: hub/project, model catalog, deployments, playground, tools, agents.
2. **Deploy GPT-4o-mini**; note the deployment name + content filter.
3. In the **playground**, set a **system message**, send a user prompt, then move **temperature** and **max tokens**.
4. Click **View code** to preview the SDK snippet (sets up Module 07).
5. Show **content filter** blocking a harmful request.

## G. Rapid recall
1. Portal URL for Foundry? *(ai.azure.com)*
2. What does code reference to call a model — base model name or **deployment name**? *(deployment name)*
3. Where do persona/rules/grounding go — system or user message? *(system)*
4. Technique to reduce hallucinations by supplying your data? *(grounding / RAG)*
5. Top-level workspace vs the solution workspace inside it? *(hub vs project)*
6. What guardrail blocks hate/violence on a deployment? *(content filter / Content Safety)*

# Module 07 — Foundry SDK, Prompts & Agents
### Day 5 · Session 1–2 | Exam Domain 2 (55–60%) — the code-aware core

The AI-901 audience profile assumes **basic Python**. You don't write production code on the exam, but you must **recognize the SDK shape**: how to connect, run a chat completion, and stand up a **single agent**. Teach learners to *read* these snippets confidently.

> ⚠️ **Facilitator note:** SDK package names and method signatures evolve. Teach the **shape and concepts** (client → messages → response; agent = model + instructions + tools → thread → run). Don't drill exact argument names.

---

## A. Setup (what to install & how auth works)

```bash
pip install openai azure-ai-projects azure-ai-inference azure-identity
```
Authentication options the exam expects you to recognize:
- **API key + endpoint** (simple; from the deployment page).
- **Microsoft Entra ID** via `DefaultAzureCredential` (keyless, recommended for production).

You need three things to call a model: **endpoint**, **credential (key or Entra)**, and the **deployment name**.

---

## B. Build a lightweight chat client with the Foundry SDK ⭐

### Option 1 — Azure OpenAI models via the `openai` SDK
```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://<your-resource>.openai.azure.com/",
    api_key="<KEY>",
    api_version="2024-10-21",
)

response = client.chat.completions.create(
    model="gpt-4o-mini",              # <-- the DEPLOYMENT name
    messages=[
        {"role": "system", "content": "You are a helpful, concise assistant."},
        {"role": "user",   "content": "Give me three tips for exam nerves."},
    ],
    temperature=0.7,
    max_tokens=300,
)
print(response.choices[0].message.content)
```

### Option 2 — Any Foundry model via `azure-ai-inference`
```python
from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import SystemMessage, UserMessage

client = ChatCompletionsClient(
    endpoint="https://<your-project-endpoint>",
    credential=AzureKeyCredential("<KEY>"),
)
result = client.complete(
    model="gpt-4o-mini",
    messages=[
        SystemMessage(content="You are a study coach."),
        UserMessage(content="Summarize responsible AI in 3 bullets."),
    ],
)
print(result.choices[0].message.content)
```

### Option 3 — Connect through a Foundry **project** with `azure-ai-projects`
```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(
    endpoint="https://<your-project-endpoint>",
    credential=DefaultAzureCredential(),
)
# Get an inference/chat client scoped to the project's deployments
chat = project.inference.get_chat_completions_client()
reply = chat.complete(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello from Foundry!"}],
)
print(reply.choices[0].message.content)
```

**Exam takeaways:** every chat call = **client + list of role-tagged messages + parameters → `response.choices[0].message.content`**. The **deployment name** is passed as `model`.

---

## C. System vs user prompts in code (recap, tested)
```python
messages=[
  {"role": "system", "content": "Rules, persona, format, grounding go HERE."},
  {"role": "user",   "content": "The user's actual request goes here."},
]
```
- Put **instructions, tone, guardrails, and grounding data** in **system**.
- Put the **request** in **user**.
- Prior **assistant** turns are included to keep conversation context (chat memory is *you* resending history — the model itself is stateless per call).

---

## D. Agents — the "agentic AI" objective ⭐

### What an agent is (memorize this equation)
> **Agent = a deployed model + instructions (system) + tools + (optional) knowledge**, that can **plan and take actions** to complete a goal — not just reply once.

| Piece | Role |
|---|---|
| **Model** | The reasoning engine (a chat/multimodal deployment) |
| **Instructions** | Persona + task + rules (like a system prompt) |
| **Tools** | Actions the agent can call: **code interpreter**, **file search / knowledge**, **function calling** (your APIs), grounding/search, etc. |
| **Threads & runs** | A **thread** holds a conversation; a **run** executes the agent over the thread (it may call tools, then respond) |

**Agent vs plain chat completion:** a chat completion is text-in/text-out. An **agent** can **use tools, retrieve knowledge, and act across multiple steps** — pick "agent" when the scenario needs *doing*, not just *answering*.

### Create & test a single agent in the Foundry portal (exam objective)
1. **Foundry → Agents → New agent.**
2. Pick the **model deployment**.
3. Write **instructions** (persona + task + rules).
4. Add **tools/knowledge** (e.g., upload files for **file search**, enable **code interpreter**, or add a **function**).
5. **Test in the playground** — chat with the agent, watch it call tools.

### Build a lightweight client for an agent (SDK) — illustrative shape
```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(endpoint="<project-endpoint>",
                          credential=DefaultAzureCredential())

# 1) Create (or reference) an agent = model + instructions + tools
agent = project.agents.create_agent(
    model="gpt-4o-mini",
    name="study-buddy",
    instructions="You are an AI-901 tutor. Be concise. Use the attached notes.",
    # tools=[...]  # e.g., file search / code interpreter / functions
)

# 2) A thread holds the conversation
thread = project.agents.create_thread()

# 3) Add a user message
project.agents.create_message(thread_id=thread.id, role="user",
                              content="Explain grounding in one line.")

# 4) Run the agent over the thread (it may call tools, then answer)
run = project.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)

# 5) Read the agent's messages
for m in project.agents.list_messages(thread_id=thread.id):
    print(m.role, ":", m.content)
```
**Exam takeaways:** the agent lifecycle is **create agent → create thread → add message → create/process run → read messages**. Tools are attached to the **agent**. A **run** is what actually executes the reasoning + tool calls.

### Multi-agent (awareness only)
Foundry supports **connected/multi-agent** solutions (agents that call other agents). AI-901 focuses on **single-agent**, but recognize the term.

---

## E. Day-5 lab checklist (do all of these hands-on)
1. **Deploy GPT-4o-mini** (if not done) and run **Option 1** chat client from a terminal.
2. Change the **system message**; show behaviour change.
3. Adjust **temperature/max_tokens** in code; observe.
4. **Portal:** build a **single agent** with instructions + a **file-search** tool over a PDF of notes; test it.
5. **SDK:** run the agent client snippet; walk the **thread → run → messages** lifecycle.

## F. Rapid recall
1. What three things do you need to call a model? *(endpoint, credential/key, deployment name)*
2. What is passed as `model=` in the SDK? *(the deployment name)*
3. Where do you read the reply? *(response.choices[0].message.content)*
4. Agent = model + ___ + ___ (+ knowledge)? *(instructions + tools)*
5. Agent lifecycle order? *(create agent → thread → message → run → read messages)*
6. Plain chat vs agent — which can use tools and act? *(agent)*
7. Keyless auth class name? *(DefaultAzureCredential / Microsoft Entra ID)*

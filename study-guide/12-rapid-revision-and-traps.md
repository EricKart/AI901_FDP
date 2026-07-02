# Module 12 — Rapid Revision & Exam Traps
### Day 6 · Session 1 | Print these. Drill them out loud in the final revision hour.

---

## A. One-page memory sheet #1 — CONCEPTS (Domain 1)

**Responsible AI — F.R.I.T.A.P.**
- **Fairness** — no bias across groups.
- **Reliability & safety** — *system* behaves consistently/safely, even in odd conditions.
- **Inclusiveness** — everyone, all abilities (accessibility).
- **Transparency** — disclose it's AI; explain how it works & its limits.
- **Accountability** — *people/orgs* answerable; governance/oversight.
- **Privacy & security** — protect data; secure the system.
> Trap: Reliability&Safety = *system*; Accountability = *people*.

**How gen-AI works**
- **Token** = text unit; billing/limits in tokens. **Embedding** = meaning vector → search/RAG.
- LLMs **predict next token** (not DB lookup) → can **hallucinate** → fix with **grounding/RAG**.
- **Multimodal** = handles images/audio too. **Reasoning (o-series)** = multi-step logic.

**Model config (⭐ #1 trap)**
- **temperature / top_p** = randomness (lower = focused/deterministic).
- **max_tokens** = length. **frequency_penalty** = less repetition. **presence_penalty** = more new topics. **seed** = reproducible. **stop** = where to halt.

**Deployment types**
- **Standard** (pay-go) · **Global Standard** (pay-go, global routing, availability) · **Provisioned/PTU** (reserved, predictable latency) · **Batch** (async bulk) · **Serverless/MaaS** (partner models, no infra) · **Managed compute** (you host).

**Workloads → capability**
- number → regression · category → classification · groups → clustering
- create content → generative · acts with tools → **agent**
- image understand → **multimodal** · image create → **image-gen**
- audio→text → **STT** · text→audio → **TTS**
- structured extract (docs/img/audio/video) → **Content Understanding**

---

## B. One-page memory sheet #2 — FOUNDRY IMPLEMENT (Domain 2)

**Foundry** = unified platform. Portal = **ai.azure.com** (no-code). SDK = same from code.
**Hub** (top workspace) → **Project** (solution) → **Deployment** (callable model).

**Deploy & call**
- Deploy a model → get a **deployment name** (what code references), endpoint, content filter.
- Chat request = list of **messages**: **system** (rules/persona/grounding) + **user** (request) + **assistant** (prior replies).
- Read reply: `resp.choices[0].message.content`.
- Auth: **API key + endpoint** or **Entra ID (DefaultAzureCredential)**.

**Prompt engineering**: clear instructions, few-shot, grounding, output-format, chain-of-thought. Rules go in **system**.

**Agents** (`agent = model + instructions + tools (+knowledge)`; can **act**)
- Lifecycle: **create agent → create thread → add message → create/process run → read messages**.
- Tools: code interpreter, **file search/knowledge**, **function calling**, grounding/search.
- Agent vs chat: agent **uses tools & acts**; chat = text-in/text-out.

**Content Understanding** = multimodal structured extraction. Define an **analyzer** + **field schema** (the fields). Works on documents, images, audio, video.

**Speech in Foundry Tools** = STT + TTS. **Multimodal audio model** = hear + reply in one.

**Safety**: content filter (Content Safety), **prompt shields** (injection), **evaluations** (groundedness/relevance/safety).

---

## C. Top 20 exam traps (drill these — this is where marks are lost)

1. **temperature ≠ length.** Randomness = temperature/top_p; length = **max_tokens**.
2. **Reliability&Safety (system) vs Accountability (people).**
3. **Deployment name**, not base model name, is used in code.
4. Rules/grounding go in the **system** message, not user.
5. **Multimodal** *understands* images; **image-generation** *creates* them.
6. **Agent** = tools + actions; a plain **chat completion** can't call your APIs on its own.
7. Agent lifecycle: **agent → thread → message → run → read**.
8. Structured extraction across files = **Content Understanding + field schema**, not ad-hoc prompting.
9. One-off question about a single image = **prompt a multimodal model**, not Content Understanding.
10. **Grounding/RAG** fixes hallucinations (not higher temperature).
11. **STT = recognition (audio→text)**; **TTS = synthesis (text→audio)**.
12. **Object detection** = boxes/location; **classification** = one label.
13. **Embeddings** = vectors for search/similarity/RAG (not generation).
14. **Reasoning (o-series)** for logic/math; **small model** for cheap/fast/high-volume.
15. **PTU** = reserved predictable latency; **Batch** = async bulk; **Global Standard** = pay-go global availability.
16. **Hub** (top) vs **Project** (solution) vs **Deployment** (model).
17. Chat models are **stateless per call**; the app resends history.
18. **Content filter** = harmful-content moderation; **prompt shields** = injection defense.
19. Legacy → current: **LUIS→CLU, QnA Maker→question answering, Form Recognizer/Video Indexer→Content Understanding, Azure AI Studio→Foundry**.
20. AI-901 assumes **basic Python + SDK/REST awareness** — recognize `client.chat.completions.create(...)` and `choices[0].message.content`.

---

## D. Final-hour verbal drill (facilitator reads, learners answer in 5s)
1. Lower temperature does what? *(more focused/deterministic)*
2. What caps response length? *(max_tokens)*
3. Agent = model + ? + ? *(instructions + tools)*
4. Fix hallucinations? *(grounding/RAG)*
5. Extract fields from invoices+audio+video? *(Content Understanding)*
6. Understand a photo → which model? *(multimodal)*  Create a photo? *(image-generation)*
7. Rules go in which message? *(system)*
8. Code references which name? *(deployment name)*
9. STT vs TTS? *(audio→text vs text→audio)*
10. Reserved predictable latency deployment? *(PTU)*
11. People answerable + governance = which principle? *(accountability)*
12. Agent lifecycle order? *(agent→thread→message→run→read)*
13. Vectors for semantic search? *(embeddings)*
14. Defend against prompt injection? *(prompt shields)*
15. Portal vs SDK? *(no-code build/test vs same from code)*

---

## E. Exam-day checklist for learners
- [ ] Passing score is **700/1000** — pace yourself; flag & return to hard items.
- [ ] Read multi-select counts ("choose TWO/THREE") carefully.
- [ ] For scenarios, first name the **workload/capability**, then the **Foundry way** to build it.
- [ ] Watch config-parameter traps (temperature vs max_tokens).
- [ ] Don't overthink code items — match the **shape** (client → messages → `choices[0].message.content`).
- [ ] Sandbox the UI first: **aka.ms/examdemo**.
- [ ] Register with a **personal Microsoft account (MSA)**, not a work/school account (records survive leaving an org).

**Good luck — you've got this. 🎯**

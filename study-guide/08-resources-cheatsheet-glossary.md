# Module 08 — Resources, Links, Decision Cheat-Sheet & Glossary

---

## A. Official Microsoft resources (share these with learners)

| Resource | Link |
|---|---|
| **AI-901 exam page** (register, logistics) | https://learn.microsoft.com/credentials/certifications/exams/ai-901/ |
| **Azure AI Fundamentals certification** | https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/ |
| **AI-901 Study Guide** (authoritative skills list) | https://aka.ms/AI901-StudyGuide |
| **Exam sandbox** (try the exam UI) | https://aka.ms/examdemo |
| **Instructor-led course AI-901T00** — "Introduction to AI in Azure" | https://learn.microsoft.com/training/courses/ai-901t00 |
| **Microsoft Foundry portal** | https://ai.azure.com |
| **Foundry docs** | https://learn.microsoft.com/azure/ai-foundry/ |
| **Azure OpenAI in Foundry docs** | https://learn.microsoft.com/azure/ai-services/openai/ |
| **Azure AI Content Understanding docs** | https://learn.microsoft.com/azure/ai-services/content-understanding/ |
| **Foundry Agent Service docs** | https://learn.microsoft.com/azure/ai-foundry/agents/ |
| **Responsible AI (Microsoft)** | https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai |
| **Azure AI Speech docs** | https://learn.microsoft.com/azure/ai-services/speech-service/ |
| **Free practice assessment** | Linked from the exam page once available (post-beta) |
| **Exam Replay / discount offers** | https://learn.microsoft.com/credentials/certifications/deals |

### Recommended free Microsoft Learn training (do the hands-on modules)
- "**Get started with AI in Azure / Microsoft Foundry**" learning path.
- "**Develop generative AI apps with Azure AI Foundry**" modules (prompts, deploy, SDK).
- "**Create agents with Azure AI Foundry**" module.
- "**Analyze content with Azure AI Content Understanding**" module.
- "**Fundamentals of responsible generative AI**" module.

---

## B. "Which capability solves this?" — poster this on the wall for all 3 days

| Scenario | Answer |
|---|---|
| Predict a **number** (price, demand) from data | Regression (ML) |
| Predict a **category** (spam/not) | Classification (ML) |
| Group unlabeled data | Clustering (ML) |
| **Create** text/code/answers | Generative AI — deploy a model in **Foundry** |
| AI that **uses tools & acts** across steps | **Agent** (Foundry Agent Service) |
| Sentiment / key phrases / entities / summary of text | **Text analysis** (model prompt or Language capability) |
| Detect the **intent** behind an utterance | CLU |
| Answer FAQs from a knowledge base | Question answering |
| Translate text | Translator |
| **Transcribe** audio → text | **Speech recognition (STT)** |
| **Speak** text → audio | **Speech synthesis (TTS)** |
| Voice assistant with one model (audio in/out) | **Multimodal model (audio)** |
| **Describe / read / reason about** an existing image | **Multimodal model (vision)** |
| **Create** a new image from text | **Image-generation model** (DALL·E / GPT-image) |
| Detect objects **and their location** | Object detection |
| One whole-image label | Image classification |
| Extract **structured fields** from invoices/receipts/IDs | **Content Understanding (documents)** |
| Extract info from **audio/video** at scale | **Content Understanding (audio/video)** |
| Reduce hallucinations using your own data | **Grounding / RAG** |
| Block hate/violent content in prompts/responses | **Content Safety / content filter** |
| More deterministic model output | Lower **temperature** |
| Limit answer length | **max tokens** |

---

## C. Legacy → current naming (say "formerly" once, then use current)

| Legacy name (AI-900 era) | Current name (AI-901) |
|---|---|
| Azure Cognitive Services | **Azure AI services** |
| Azure AI Studio / Azure AI Foundry | **Microsoft Foundry** |
| Computer Vision | Azure AI Vision / **multimodal model** |
| Form Recognizer / Document Intelligence | **Azure Content Understanding** (documents) |
| Video Indexer | **Azure Content Understanding** (video) |
| LUIS | **Conversational Language Understanding (CLU)** |
| QnA Maker | **Custom question answering** |
| Anomaly Detector | (retiring) |
| Text Analytics | **Azure AI Language** (text analysis features) |

---

## D. 7-day self-study plan (give to learners for after the camp)
1. **Day 1:** Responsible AI + AI workloads + how gen-AI models work (Modules 01–02). Practice Test 1 Q1–20.
2. **Day 2:** Model selection, deployment types, config parameters (Module 02). Deploy a model in Foundry.
3. **Day 3:** Text analysis + computer vision + image generation (Modules 03–04). Playground labs.
4. **Day 4:** Speech + Content Understanding (Module 05). Run an analyzer.
5. **Day 5:** Foundry SDK chat client + prompts (Modules 06–07). Run the code.
6. **Day 6:** Build & test a single agent (Module 07). Practice Test 2.
7. **Day 7:** Full Exam Simulation (Module 11) + review traps (Module 12) + official practice assessment.

---

## E. Glossary (fast reference)

- **Token** — smallest text unit a model reads/writes; billing & limits are in tokens.
- **Embedding** — numeric vector of meaning; powers search/similarity/RAG.
- **LLM / SLM** — large / small language model.
- **Transformer** — architecture using **attention** behind modern LLMs.
- **Multimodal model** — handles more than text (images/audio).
- **Context window** — max tokens considered at once (prompt + response).
- **Prompt (system/user/assistant)** — role-tagged messages steering a chat model.
- **Temperature / top_p** — output randomness/creativity.
- **max_tokens** — output length cap.
- **frequency/presence penalty** — repetition / new-topic control.
- **Grounding / RAG** — supplying retrieved data to reduce hallucination.
- **Hallucination** — confident but false model output.
- **Agent** — model + instructions + tools that can act; runs over a **thread** via a **run**.
- **Tool** — an action an agent can call (code interpreter, file search, function).
- **Foundry** — Microsoft's unified AI platform (portal + SDK).
- **Hub / project** — Foundry workspace hierarchy.
- **Deployment** — a model made callable (deployment name + endpoint + filter).
- **Deployment types** — Standard, Global Standard, Provisioned (PTU), Batch, Serverless, Managed compute.
- **Content Understanding** — multimodal structured extraction (docs/images/audio/video) via an **analyzer** + **field schema**.
- **Content Safety / content filter** — responsible-AI moderation of prompts & responses.
- **Prompt shield** — defense against prompt-injection/jailbreak.
- **Evaluations** — quality tests (groundedness, relevance, safety).
- **STT / TTS** — speech-to-text / text-to-speech.
- **CLU** — Conversational Language Understanding (intent + entities).

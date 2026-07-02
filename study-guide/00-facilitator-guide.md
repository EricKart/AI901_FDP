# AI-901 (Microsoft Azure AI Fundamentals) — Faculty Development Programme Kit
### Facilitator's Master Guide & Timeline Delivery Plan
**Built against the official AI-901 skills measured, updated 15 April 2026.**

---

## 0. Read this first — AI-901 is NOT the old AI-900

Your programme is correctly branded **AI-901**. Microsoft **retired AI-900 on 30 June 2026** and replaced it with **AI-901**, which is a **ground-up redesign**, not a rename. If you teach the old AI-900 syllabus (individual Cognitive Services in isolation, no coding), your learners **will fail.** The three structural changes:

1. **The exam is now hands-on and code-aware.** The official audience profile requires *"knowledge of **Python coding syntax and programming techniques**"* and familiarity with *"**REST APIs, SDKs, and CLIs**."* AI-900 required no coding. AI-901 does.
2. **Everything routes through Microsoft Foundry** (formerly *Azure AI Foundry* / *Azure AI Studio*): the Foundry **portal**, model **deployment**, the Foundry **SDK**, and the **Foundry Agent Service**. **55–60% of the exam** is *implementing* solutions in Foundry.
3. **"Information extraction" = Azure Content Understanding** (one multimodal service across documents, images, audio, video) — **not** Form Recognizer / Document Intelligence / Video Indexer as separate products.

> **One-line positioning for your learners:** *"AI-900 asked 'which service does this?' AI-901 asks 'build it in Foundry — deploy a model, prompt it, wire up an agent, extract info with Content Understanding.'"*

---

## 1. The exam — facts to state on Day 1

| Fact | Detail |
|---|---|
| Exam code | **AI-901** |
| Certification | Microsoft Certified: Azure AI Fundamentals |
| Level | Fundamentals — but now assumes basic Python literacy |
| **Passing score** | **700 / 1000** (scaled; **not** 70% of questions) |
| Questions | ~**40–60** (Microsoft doesn't publish an exact count) |
| Duration | ~**45–60 min** exam time (~65 min seat time) |
| Cost | ~**USD $99** (regional pricing varies; MCT/partner discounts exist) |
| Delivery | Online proctored **or** Pearson VUE centre |
| Languages | **English first**; localized versions ~8 weeks later. Non-native speakers may request **+30 min** |
| Validity | Fundamentals certifications **do not expire** |
| Question formats | Single MCQ, multiple-select ("choose two/three"), **drag-and-drop / build-list**, **hot-area yes/no matrix**, dropdown-in-sentence, **code-completion / "complete the code" hot-area**. No case studies, no live labs |
| Note from Microsoft | *"Most questions cover **GA** features; Preview features may appear if commonly used. Be familiar with **REST APIs, SDKs, and CLIs**."* |

### Official skills measured (as of 15 April 2026) — memorize this table
| Domain | Weight | Sub-skills |
|---|---|---|
| **1. Identify AI concepts and capabilities** | **40–45%** | • **Responsible AI** — fairness, reliability & safety, privacy & security, inclusiveness, transparency, accountability<br>• **AI model components & configuration** — how generative AI models work; pick a model by capability; deployment options & config parameters<br>• **AI workloads** — generative/agentic AI, text analysis, speech, computer vision, information extraction; text-analysis techniques (keyword extraction, entity detection, sentiment, summarization); speech recognition & synthesis; computer vision & image-generation models; extracting info from text/images/audio/video |
| **2. Implement AI solutions by using Microsoft Foundry** | **55–60%** | • **Gen-AI apps & agents** — write system & user prompts; deploy & interact with a model in the Foundry portal; build a lightweight **chat client with the Foundry SDK**; create & test a **single-agent** solution; build an agent client app<br>• **Text & speech** — lightweight text-analysis app; respond to **spoken prompts with a multimodal model**; app using **Azure Speech in Foundry Tools**<br>• **Computer vision & image generation** — interpret **visual input with a multimodal model**; generate **visual outputs**; lightweight vision app<br>• **Information extraction** — extract from **documents/forms, images, audio, video** using **Azure Content Understanding in Foundry Tools**; lightweight extraction app |

> **Coach's takeaway:** More than half the exam is "can you *do* it in Foundry?" Your FDP must be **lab-first**. Slides + memorization alone are an AI-900 strategy and will underperform.

---

## 2. This kit — file map

| File | Purpose | Maps to exam |
|---|---|---|
| `00-START-HERE-Facilitator-Guide.md` | This guide, exam facts, delivery plan | — |
| `01-Responsible-AI-and-AI-Workloads.md` | 6 principles + workload taxonomy | Domain 1 |
| `02-How-GenAI-Models-Work-and-Model-Config.md` | Tokens, transformers, model selection, **deployment & parameters** | Domain 1 |
| `03-Computer-Vision-and-Image-Generation.md` | CV concepts + multimodal vision + image generation | Domains 1 & 2 |
| `04-Text-Analysis-and-NLP.md` | Text-analysis techniques + Foundry text apps | Domains 1 & 2 |
| `05-Speech-and-Information-Extraction.md` | Speech + **Azure Content Understanding** | Domains 1 & 2 |
| `06-Microsoft-Foundry-Portal-and-Deployment.md` | Portal, model catalog, deploy, playground, prompts | Domain 2 |
| `07-Foundry-SDK-Prompts-and-Agents.md` | **Python SDK code, chat client, single-agent solution** | Domain 2 |
| `08-Resources-Links-Cheatsheet-Glossary.md` | Official links, decision table, glossary | All |
| `09-Practice-Test-1-HARD.md` | 40 hard Q + explained answers | All |
| `10-Practice-Test-2-HARD.md` | 40 hard Q + explained answers | All |
| `11-FULL-EXAM-SIMULATION.md` | 50-Q timed mock, exam-authentic | All |
| `12-Rapid-Revision-and-Exam-Traps.md` | Day-6 memory sheets + trap list | All |

---

## 3. Timeline-wise delivery plan (remapped to AI-901)

Your grid was written with AI-900 topic names. Here is what each session **actually** needs to deliver for AI-901. **Bold = new for AI-901 that was NOT in the old syllabus.**

### DAY 3 (07-Jul-26) — Foundations, Responsible AI, **Foundry orientation**, Vision
| Slot | Your grid says | Deliver this | Files |
|---|---|---|---|
| **S1 9:30–11:15** | Intro to AI-901, Azure AI Services & Responsible AI | AI workload taxonomy; **6 Responsible AI principles** (free marks); **how generative AI models work at a high level**; **tour of the Microsoft Foundry portal + model catalog** (set the stage — everything lives here now) | `01`, `02`, `06` |
| **S2 11:30–1:15** | Computer Vision & Azure AI Vision | CV concepts (classification/detection/OCR); **image-generation models (DALL·E / GPT-image)**; **LAB: interpret an image with a multimodal model in the Foundry playground; generate an image** | `03`, `06` |
| Self-practice 2:15–4:30 | — | **LAB: deploy a model in Foundry** (`06`); Practice Test 1 Q1–20 | `06`, `09` |

### DAY 4 (08-Jul-26) — Language, Speech, **Content Understanding**
| Slot | Your grid says | Deliver this | Files |
|---|---|---|---|
| **S1 9:30–11:15** | NLP & Azure AI Language | Text-analysis techniques: **keyword extraction, entity detection, sentiment, summarization**; **LAB: build a lightweight text-analysis app / prompt a model to analyze text in Foundry** | `04` |
| **S2 11:30–1:15** | Speech AI & Document Intelligence | Speech recognition & synthesis concepts; **Azure Speech in Foundry Tools**; **respond to spoken prompts with a multimodal model**; **Azure Content Understanding** for documents/images/audio/video (this *replaces* the old "Document Intelligence" teaching) | `05` |
| Self-practice 2:15–4:30 | — | **LAB: extract fields from a sample invoice/receipt with Content Understanding**; Practice Test 1 Q21–40 | `05`, `09` |

### DAY 5 (09-Jul-26) — Generative AI, **Agents**, Foundry SDK (the heart of the exam)
| Slot | Your grid says | Deliver this | Files |
|---|---|---|---|
| **S1 9:30–11:15** | Generative AI, AI Agents & Azure OpenAI | **System vs user prompts & prompt engineering**; **deploy & chat with a model in Foundry**; **LAB: build a lightweight chat client with the Foundry SDK (Python)**; **create & test a single agent in the Foundry portal** | `02`, `06`, `07` |
| **S2 11:30–1:15** | AI-901 cert prep & integrated Azure AI practice | **Model deployment options & config parameters** (temperature, max tokens, top_p, etc.); grounding/RAG concept; **Content Safety**; run **Practice Test 2** as a live workshop; exam logistics | `02`, `07`, `10` |
| Self-practice 2:15–4:30 | — | **LAB: give the agent a tool/knowledge and re-test**; official study-guide review | `07`, `08` |

### DAY 6 (10-Jul-26) — Revision + Mock Certification Test
| Slot | Your grid says | Deliver this | Files |
|---|---|---|---|
| S1 9:30–11:15 | Practical sessions / Revision | Rapid revision with one-page memory sheets; drill **exam traps** (Foundry vs Content Understanding vs Agents; model-config parameters; prompt roles) | `12` |
| S2 11:30–1:15 | Mock Certification Test | Administer **Full Exam Simulation (50 Q, 60 min)**, then review **every** answer | `11` |

---

## 4. Pre-programme setup checklist (do this BEFORE Day 3)

Because AI-901 is lab-first, sort logistics in advance:
- [ ] Each learner has an **Azure account** (Azure free account, **Azure for Students**, or a lab tenant you provide).
- [ ] You can create a **Microsoft Foundry** project + hub in a region that offers the needed models (e.g., GPT-4o / GPT-4o-mini and an image model like DALL·E 3 / GPT-image).
- [ ] **Azure OpenAI / Foundry model access** is enabled for your tenant (some deployments require the subscription to be approved).
- [ ] Python 3.10+ installed, plus `pip install openai azure-ai-projects azure-ai-inference azure-identity` (see `07`).
- [ ] **VS Code** (optional but recommended) for the SDK labs.
- [ ] Budget guard-rails: use **GPT-4o-mini** / small models and low token limits for labs; **delete deployments** after class.
- [ ] Bookmark the portals: **Foundry portal (ai.azure.com)**, Azure portal, and the **exam sandbox** (`aka.ms/examdemo`).

---

## 5. How to teach AI-901 (meta-strategy)

1. **Lab beats slide.** For every concept, do a 5-minute Foundry demo. The exam tests whether learners recognize what the portal/SDK actually does.
2. **Scenario → capability mapping is still ~40%.** "Extract the total from scanned receipts" → **Content Understanding**. "Describe what's in this photo" → **multimodal model (vision)**. "Group customers with no labels" → clustering. Drill pattern recognition.
3. **The Implement half rewards familiarity with the moving parts:** the **system message**, a **deployed model name/endpoint**, the **SDK client**, an **agent = model + instructions + tools**, and an **analyzer/field-schema** in Content Understanding.
4. **Kill the AI-901 confusable pairs** (full list in `12`):
   - **Foundry portal** (build/deploy/test in the UI) vs **Foundry SDK** (do it from code)
   - **System prompt** (persona/rules/grounding) vs **user prompt** (the request)
   - **Chat model** vs **multimodal model** (accepts images/audio) vs **image-generation model** (produces images)
   - **Content Understanding** (extract structured info from files) vs **prompting a multimodal model** (reason over one image/doc ad-hoc)
   - **Agent** (has tools + can act) vs **plain chat completion** (text in → text out)
   - **temperature/top_p** (randomness) vs **max tokens** (length) vs **frequency/presence penalty** (repetition)
5. **Responsible AI = guaranteed marks.** Six principles, unchanged from AI-900. Anchor them (see `01`).

## 6. Do / Don't
- ✅ Get every learner to **deploy one model and run one chat completion** before Day 5.
- ✅ Show real, runnable **Python** — even non-coders must recognize the SDK shape.
- ✅ Keep a "which capability solves this?" poster up all 3 days (`08`).
- ❌ Don't teach retired branding as current: *Cognitive Services, Form Recognizer, LUIS, QnA Maker, Anomaly Detector* are **legacy**. Mention once as "formerly," then use current names (**Microsoft Foundry, Content Understanding, Conversational Language Understanding, Azure OpenAI in Foundry**).
- ❌ Don't skip the coding labs because "it's just fundamentals" — the audience profile changed.

**Next:** open `01-Responsible-AI-and-AI-Workloads.md`.

---
*Source of truth for objectives: Microsoft Learn — AI-901 exam page and study guide (`aka.ms/AI901-StudyGuide`), skills measured as of 15 April 2026.*

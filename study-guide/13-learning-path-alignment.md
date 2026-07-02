# Module 13 — Official Learning-Path Alignment (Crosswalk)
### Map every Microsoft Learn module/unit to this kit — use as the coverage checklist

AI-901 is backed by **two official Microsoft Learn learning paths**. This file proves the kit covers **every unit** and points you to the exact study-guide module + slide deck + lab for each.

---

## Learning Path 1 — "AI concepts for developers and technology professionals" → **Domain 1 (Identify, 40–45%)**

| Official module → unit | Covered in | Slide deck | Lab |
|---|---|---|---|
| **Introduction to AI concepts** — Intro to AI; Generative AI & agents; Text & NLP; Speech; Computer vision; Information extraction; Responsible AI; *Explore AI workloads* | `01`, `02` (overview) | Day 3 | — |
| **Introduction to generative AI and agents** — LLMs; Prompts; AI agents | `02`, `07` | Day 5 | Lab 2, 3 |
| **Introduction to NLP concepts** — Tokenization; Statistical text analysis; Semantic language models | `04` (Part 0) | Day 4 | Lab (text) |
| **Introduction to AI speech concepts** — Speech recognition; Speech synthesis | `05` (Part A) | Day 4 | Lab (speech) |
| **Introduction to computer vision concepts** — CV tasks/techniques; Images & image processing; **CNNs**; **Vision transformers & multimodal**; Image generation | `03` (Part A) | Day 3 | — |
| **Introduction to AI-powered information extraction** — Overview; **OCR**; **Field extraction & mapping** | `05` (Part B) | Day 4 | Lab 4 |

### Two concepts to nail from this path (added detail)
- **OCR (Optical Character Recognition)** — the classic technique to detect and read **text within images/scans**; the first step of most document extraction. In AI-901 this feeds **Content Understanding** and multimodal reading.
- **Field extraction & mapping** — going beyond raw OCR text to **map values to named fields** (e.g., this number → `total`, this date → `invoice_date`). That mapping is exactly what a Content Understanding **field schema** defines.

---

## Learning Path 2 — "Get started with AI applications and agents on Azure" → **Domain 2 (Implement, 55–60%)**

| Official module → unit | Covered in | Slide deck | Lab |
|---|---|---|---|
| **Get started with AI in Azure** — Understand Azure; Developing AI apps on Azure; **Microsoft Foundry for AI**; **Using Foundry endpoints**; *Exercise* | `06` | Day 3/5 | Lab 1 |
| **Get started with generative AI and agents** — Generative AI models; Using a model; **Creating an agent**; *Exercise* | `02`, `06`, `07` | Day 5 | Lab 2, 3 |
| **Get started with text analysis** — Understand text analysis in Foundry; **Create a client app that analyzes text**; **Use Azure Language with an agent**; *Exercise* | `04` (Part B) | Day 4 | Lab (text) |
| **Get started with speech** — Speech recognition; Speech synthesis; **Creating a speech-capable agent**; *Exercise* | `05` | Day 4 | Lab (speech) |
| **Get started with computer vision** — **Multimodal models for image analysis**; **Image generation models**; **Video generation models**; *Exercise* | `03` (Part B) | Day 3 | — |
| **Get started with information extraction** — **Extract from documents**; **Extract from audio & video** (Content Understanding); *Exercise* | `05` (Part B) | Day 4 | Lab 4 |

### Three implementation patterns to nail from this path (added detail)
- **Create a client application that analyzes text** — a lightweight **Python** app that either (a) prompts a deployed model or (b) calls **Azure Language in Foundry Tools**, then prints structured results. (See `07` chat-client shape.)
- **Use Azure Language / Speech *with an agent*** — attach text-analysis or speech as a **tool/knowledge** to an **agent**, so the agent can analyze text or talk. Reinforces *agent = model + instructions + tools*.
- **Speech-capable agent** — an agent wired with **Azure Speech (STT/TTS)** so users can **talk to it** and hear replies; or use a **multimodal audio model** for a simpler single-model voice loop.

---

## Coverage self-check (tick before the exam)
- [ ] I can define token, embedding, transformer, CNN, vision transformer, multimodal.
- [ ] I can name the 6 responsible-AI principles and give a consideration for each.
- [ ] I can tell statistical vs semantic text analysis apart.
- [ ] I can pick image-generation vs video-generation vs multimodal.
- [ ] I can deploy a model, find its **endpoint**, and call it with the SDK.
- [ ] I can write a system + user prompt and read `choices[0].message.content`.
- [ ] I can build a single **agent** (model + instructions + tools) and run it.
- [ ] I can extract fields with **Content Understanding** (analyzer + field schema) from docs/images/audio/video.
- [ ] I can wire text/speech to an agent.

**Official paths:** linked in [08-resources-cheatsheet-glossary.md](08-resources-cheatsheet-glossary.md).

# Module 02 — How Generative AI Models Work + Model Selection, Deployment & Config
### Day 3 S1 / Day 5 | Exam Domain 1: "Identify AI model components and configurations"

This is one of the **most-tested new areas** in AI-901. Three sub-skills: (A) how gen-AI models work, (B) pick a model by capability, (C) deployment options & configuration parameters.

---

## PART A — How generative AI models work (conceptual, no math)

**Generative AI** produces new content — text, code, images, audio — by predicting likely output from patterns learned in massive training data.

### Key concepts to recognize
| Term | Plain meaning |
|---|---|
| **Large Language Model (LLM)** | A model trained on huge text corpora that generates text by predicting the next token |
| **Small Language Model (SLM)** | Smaller, cheaper, faster model (e.g., Microsoft **Phi**) for lighter tasks / edge |
| **Transformer** | The neural-network architecture behind modern LLMs; uses **attention** to weigh relationships between tokens |
| **Token** | The unit a model reads/writes — roughly a word-piece (~4 chars / ~¾ of a word in English). Billing & limits are in **tokens** |
| **Tokenization** | Splitting text into tokens before the model processes it |
| **Embedding** | A numeric **vector** representing the meaning of text/image; similar meanings → nearby vectors. Powers **search, similarity, RAG** |
| **Context window** | Max tokens a model can consider at once (prompt + response) |
| **Prompt / completion** | Your input / the model's generated output |
| **Pretraining vs fine-tuning** | Learn general language first; optionally adapt to your data/task later |
| **Multimodal model** | Accepts and/or produces **more than text** — e.g., images + text + audio (GPT-4o is multimodal) |
| **Hallucination** | Model states something plausible but **false**; mitigate with **grounding/RAG** |
| **Grounding / RAG** (Retrieval-Augmented Generation) | Supply the model with your **retrieved data** so answers are based on facts, not just training memory |

### How a chat model "thinks" (the mental model to teach)
1. Your prompt is **tokenized**.
2. The transformer predicts the **next token**, then the next, one at a time (**autoregressive**), guided by **attention** over the context.
3. Sampling settings (temperature/top_p) decide how "creative" vs deterministic the choice is.
4. It stops at a **stop condition** or the **max token** limit.

> **Exam trap:** LLMs **predict tokens**, they don't "look up" a database. That's why they can hallucinate — and why **grounding/RAG** matters.

---

## PART B — Identify an appropriate model by capability

The exam gives a need → you pick the **type** of model. Know these families (all available in the **Foundry model catalog**):

| Need | Model type | Examples in Foundry |
|---|---|---|
| Chat / reasoning / summarization / text generation | **Chat / LLM** | GPT-4o, GPT-4o-mini, GPT-4.1, **o-series reasoning models** |
| Cheap/fast/simple text at scale | **Small model** | GPT-4o-mini, **Phi** family |
| Understand **images + text together** | **Multimodal** | GPT-4o (vision), GPT-4.1 |
| **Generate images** from text | **Image-generation** | **DALL·E 3**, **GPT-image** |
| Convert text → **vectors** for search/similarity/RAG | **Embeddings** | text-embedding-3-large / -small, ada-002 |
| Speech to text / text to speech | **Speech** models | Azure Speech (in Foundry Tools) |
| Open-source / specialized | **Partner models** | Meta **Llama**, **Mistral**, **Cohere**, etc. |

Selection factors the exam may probe: **capability/modality**, **cost**, **latency/speed**, **context-window size**, **quality vs price trade-off**, **region/quota availability**, and **whether it's GA or preview**.

> **Exam trap — reasoning vs chat:** *"complex multi-step logic/math"* → an **o-series reasoning model**. *"fast, high-volume, simple replies"* → a **small model** (GPT-4o-mini / Phi). *"analyze an uploaded photo"* → a **multimodal** model. *"create a picture"* → an **image-generation** model.

---

## PART C — Deployment options & configuration parameters ⭐ (heavily tested)

Before you can call a model, you must **deploy** it in Foundry. You choose a **deployment type** and set **inference parameters**.

### Deployment types (know the trade-offs)
| Deployment type | What it means | When |
|---|---|---|
| **Standard** | Pay-per-token, regional | General use, dev/test |
| **Global Standard** | Pay-per-token, routed across Microsoft's global capacity | Best availability/throughput for pay-go |
| **Provisioned Throughput (PTU)** | Reserved dedicated capacity, predictable latency | High, steady production load |
| **Batch** | Async, large jobs at lower cost | Non-real-time bulk processing |
| **Serverless API (Models-as-a-Service)** | Call partner/open models via API, no infra | Use Llama/Mistral/etc. without hosting |
| **Managed compute** | You host the model on dedicated VMs | Full control / custom models |

You also get a **deployment name** (what you reference in code), an **endpoint**, and **keys / Entra ID** auth.

### Inference configuration parameters (memorize what each does)
| Parameter | Controls | Effect | Exam cue |
|---|---|---|---|
| **temperature** (0–2) | Randomness | Higher = more creative/varied; lower = more focused/deterministic | *"more deterministic/consistent"* → **lower temperature** |
| **top_p** (0–1) | Nucleus sampling | Alternative to temperature; lower = considers fewer, likelier tokens | *"limit to most probable words"* → lower top_p |
| **max_tokens / max_completion_tokens** | Output **length** cap | Caps response size (and cost) | *"limit response length"* → **max tokens** |
| **stop sequences** | Where to stop | Model halts when it emits the sequence | *"stop when it reaches X"* |
| **frequency_penalty** | Repetition of frequent tokens | Higher = discourages repeating the same words | *"reduce repetition"* |
| **presence_penalty** | Introducing new topics | Higher = pushes toward new topics/words | *"encourage new topics"* |
| **seed** | Reproducibility | Same seed + inputs → more repeatable output | *"reproducible results"* |
| **system message** | Model behaviour/persona/rules | Sets role, tone, guardrails, grounding | (see Module 07) |

> **The #1 config trap:** *temperature/top_p = randomness*, **NOT length**. *max_tokens = length*, **NOT creativity**. Don't mix them up — it's a favourite distractor.

### Prompt roles (bridges to Module 07)
A chat request is a list of **messages** with roles:
- **system** — instructions/persona/rules/grounding (highest-level steering).
- **user** — the human's request.
- **assistant** — the model's replies (and prior turns for context).

---

## D. Live-demo checklist
1. In **Foundry → Deployments**, deploy **GPT-4o-mini**; show the **deployment name**, endpoint, and **content filter**.
2. In the **playground**, move the **temperature** slider from 0 → 1.5 on the same prompt; show output variance.
3. Set **max tokens** low; show the response getting cut off.
4. Paste text and ask for embeddings conceptually; explain vectors → search/RAG.

## E. Rapid recall
1. Unit of text a model processes & bills on? *(token)*
2. "More deterministic output" → change which parameter, which way? *(lower temperature)*
3. "Limit how long the answer is" → which parameter? *(max tokens)*
4. Numeric vector representing meaning, used for search? *(embedding)*
5. Feeding retrieved facts into the prompt to reduce hallucination? *(grounding / RAG)*
6. Complex multi-step reasoning → which model type? *(reasoning / o-series)*
7. Steady, high-volume production with predictable latency → which deployment? *(Provisioned Throughput / PTU)*
8. Which message role sets the persona and rules? *(system)*

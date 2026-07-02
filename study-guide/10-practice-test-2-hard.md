# Practice Test 2 — HARD (AI-901)
**40 questions · trickier · mixed formats (MCQ, multi-select, yes/no matrix, complete-the-code).**
Recommended time: 45 min. Pass ≈ 28/40. Run this as the Day-5 live workshop. Answers at bottom.

---

## Questions

**Q1.** A model must summarize legal contracts. Legal insists answers use ONLY the uploaded contract text and cite nothing else. Which combination BEST enforces this?
A. High temperature + long max_tokens
B. A **system message** restricting scope + **grounding** the contract text into the prompt
C. presence_penalty = 2 + seed
D. An image-generation model

**Q2.** (Multi-select) Which THREE are configuration/inference parameters, not deployment types? (Choose THREE)
A. temperature  B. Provisioned Throughput  C. top_p  D. max_tokens  E. Global Standard

**Q3.** Match the workload. *"An app that reasons over a customer's uploaded photo of a damaged part AND then files a warranty claim through a ticketing API."* This needs:
A. A single chat completion
B. A **multimodal model** (to read the image) **plus an agent** (to call the ticketing tool)
C. Only an embeddings model
D. Speech synthesis

**Q4.** **Yes/No matrix.** For each statement, is it TRUE?
1) An agent can call tools such as code interpreter or a custom function.
2) A plain chat completion can autonomously call your external APIs without you wiring tools.
3) A run in the Agent Service may invoke tools before returning a response.
(Choose the correct Yes/No set)
A. Yes / No / Yes  B. Yes / Yes / Yes  C. No / No / Yes  D. Yes / No / No

**Q5.** A startup needs the **cheapest, fastest** model for very high volumes of short, simple replies. Best choice?
A. An o-series reasoning model  B. A small model (e.g., GPT-4o-mini / Phi)  C. DALL·E 3  D. A large multimodal model at max settings

**Q6.** **Complete the code.** Fill the blank so the reply text prints:
```python
resp = client.chat.completions.create(model="gpt-4o-mini", messages=msgs)
print(resp.___)
```
A. choices[0].message.content
B. deployment.name
C. usage.tokens.text
D. system.message

**Q7.** Which principle is chiefly addressed by running **fairness/bias assessments** across demographic groups before release?
A. Reliability & safety  B. Fairness  C. Transparency  D. Privacy & security

**Q8.** A bank wants structured extraction of fields from **passport images and PDFs of forms**, plus the **same** approach for **onboarding call recordings**. Which single service covers all three?
A. Azure AI Translator  B. Azure Content Understanding  C. Custom Vision  D. Azure AI Language only

**Q9.** Which statement about **max_tokens vs temperature** is correct?
A. Both control creativity  B. max_tokens caps length; temperature controls randomness  C. Both control length  D. temperature caps length; max_tokens controls randomness

**Q10.** You must **transcribe** multilingual webinars into text and later **read** answers aloud in a chatbot. Which two capabilities? (Choose TWO)
A. Speech recognition (STT)  B. Object detection  C. Speech synthesis (TTS)  D. Image generation

**Q11.** In Foundry, the value you reference from code to invoke a specific model instance is the:
A. Hub name  B. Region  C. Deployment name  D. Content filter name

**Q12.** A generative feature must avoid producing hateful or violent content. Which control do you configure on the deployment?
A. Content filter (Content Safety)  B. top_p  C. Batch size  D. Seed

**Q13.** (Multi-select) Which TWO are true about **embeddings**? (Choose TWO)
A. They convert text to numeric vectors  B. They generate images  C. Similar meanings map to nearby vectors  D. They are a responsible-AI principle

**Q14.** Which scenario is a poor fit for an **agent** and better as a single completion?
A. "Fetch today's exchange rate via API and convert the invoice"  B. "Rewrite this paragraph more formally"  C. "Search my files then draft and send an email"  D. "Look up the order status and notify the customer"

**Q15.** **Yes/No matrix.** How generative models work — TRUE?
1) LLMs predict the next token based on context.
2) LLMs always retrieve answers from a connected database.
3) Grounding/RAG can reduce hallucinations.
A. Yes / No / Yes  B. Yes / Yes / Yes  C. No / No / Yes  D. Yes / No / No

**Q16.** A team wants **predictable, reserved throughput** for a customer-facing assistant with strict latency SLAs. Which deployment type?
A. Batch  B. Provisioned Throughput (PTU)  C. Free tier  D. Serverless spot

**Q17.** Which correctly maps the message role to its job?
A. user = persona & rules  B. system = the human's request  C. system = persona, rules, grounding; user = the request  D. assistant = deployment settings

**Q18.** A retailer wants to **create** lifestyle product images from text briefs. Which model?
A. Embeddings  B. DALL·E 3 / GPT-image (image-generation)  C. Speech  D. Reasoning model

**Q19.** Which is the BEST description of **Azure Content Understanding**?
A. A chat model  B. A service that extracts structured info from documents, images, audio, and video using analyzers/field schemas  C. A speech-only transcription tool  D. A vector database

**Q20.** For an **extraction** task you want stable, non-creative output. Set temperature to:
A. 2.0  B. ~0  C. 1.0  D. It has no effect

**Q21.** (Multi-select) Which TWO belong to the "Implement AI solutions by using Microsoft Foundry" domain? (Choose TWO)
A. Deploy a model and interact with it in the Foundry portal
B. Describe the six responsible-AI principles
C. Create and test a single-agent solution
D. Define what a token is

**Q22.** A model must answer questions grounded in a 400-page manual too large to fit in one prompt. Best approach?
A. Paste the whole manual every call  B. RAG: retrieve relevant chunks (via embeddings/search) and add them to the prompt  C. Raise temperature  D. Use image generation

**Q23.** Which is an example addressing **reliability & safety**?
A. Publishing a transparency note  B. Extensive testing so the system behaves safely under unexpected inputs  C. Redacting personal data  D. Adding captions for accessibility

**Q24.** **Complete the code.** To attach an image for a vision question, the image goes in the ___ message content:
```python
messages=[{"role":"system","content":"..."},
          {"role":"____","content":[{"type":"text","text":"Describe it"},
                                     {"type":"image_url","image_url":{"url":URL}}]}]
```
A. system  B. user  C. assistant  D. tool

**Q25.** Which pair are BOTH legacy names replaced in AI-901?
A. Foundry & Content Understanding  B. LUIS & QnA Maker  C. GPT-4o & DALL·E  D. Hub & Project

**Q26.** A field schema defines:
A. The model's temperature  B. The specific fields Content Understanding should extract  C. The agent's tools  D. The deployment type

**Q27.** Which is TRUE about **agents vs multimodal models**?
A. They are the same thing  B. An agent adds instructions + tools + the ability to act; a multimodal model adds image/audio understanding — they can be combined  C. Multimodal models cannot be used by agents  D. Agents cannot use tools

**Q28.** A customer wants **semantic search** so "car" also matches "automobile." Which underpins this?
A. Object detection  B. Embeddings + vector similarity  C. Speech synthesis  D. Higher max_tokens

**Q29.** Which responsible-AI principle covers **de-identifying training data and obtaining consent**?
A. Inclusiveness  B. Privacy & security  C. Transparency  D. Reliability & safety

**Q30.** You need the model to **stop** generating when it outputs `###`. Which parameter?
A. stop sequence  B. temperature  C. presence_penalty  D. seed

**Q31.** (Multi-select) Which TWO are valid model **types** in the Foundry catalog? (Choose TWO)
A. Embeddings model  B. Field schema  C. Multimodal model  D. Content filter

**Q32.** A scenario: *"Detect and locate every defective weld in a photo of a pipeline."* Best capability?
A. Image classification  B. Object detection  C. Summarization  D. Speech recognition

**Q33.** Which BEST reduces **prompt-injection** risk in a deployed assistant?
A. Prompt shields + strict system message  B. Higher temperature  C. Larger context window only  D. Batch deployment

**Q34.** For a **single-agent** solution tested in the portal, the minimum you must define is:
A. Only a hub  B. A model deployment + instructions (+ optional tools)  C. A field schema  D. A speech voice

**Q35.** Which is a correct statement about **deployment types**?
A. Batch is best for real-time chat  B. Global Standard routes pay-go traffic across global capacity for better availability  C. PTU is billed per token with no reservation  D. Serverless requires you to manage VMs

**Q36.** A team wants a model to **explain its step-by-step reasoning** for a tricky logic task. Which technique/model helps MOST?
A. Lowering max_tokens  B. Chain-of-thought prompting and/or a reasoning model  C. Image generation  D. Disabling the content filter

**Q37.** **Yes/No matrix.** Content Understanding — TRUE?
1) It can extract fields from video.
2) It uses a field schema to define outputs.
3) It is only for real-time chat.
A. Yes / Yes / No  B. No / Yes / No  C. Yes / No / Yes  D. Yes / Yes / Yes

**Q38.** Which is the correct order to go from zero to a working chat call in Foundry?
A. Write code → deploy model → create project  B. Create project → deploy model → call the deployment from portal/SDK  C. Call model → create hub → deploy  D. Deploy agent → delete project → call

**Q39.** A company must **disclose limitations** of its AI diagnosis tool to clinicians. Which principle, and which artifact helps?
A. Fairness; a bias report  B. Transparency; a transparency note / clear system disclosure  C. Privacy; an NDA  D. Accountability; a PTU

**Q40.** Which single sentence best captures AI-901's shift from AI-900?
A. It removed responsible AI  B. It moved from naming isolated services to **implementing solutions in Microsoft Foundry** (models, agents, Content Understanding) with basic coding  C. It is now only about machine learning math  D. It dropped generative AI

---

## Answer Key & Explanations

**Q1 — B.** Scope enforcement lives in the **system message**; making it use only the contract requires **grounding** that text into the prompt. Penalties/temperature/images don't enforce sourcing.

**Q2 — A, C, D.** temperature, top_p, max_tokens are inference parameters. Provisioned Throughput & Global Standard are **deployment types**.

**Q3 — B.** Reading the image = multimodal; filing a claim via API = agent with a tool. Combine both.

**Q4 — A (Yes/No/Yes).** Agents use tools; plain completions can't autonomously call your APIs without tool wiring; a run may call tools before answering.

**Q5 — B.** Small models (GPT-4o-mini / Phi) are cheapest/fastest for high-volume simple tasks.

**Q6 — A.** `resp.choices[0].message.content` holds the reply.

**Q7 — B. Fairness.** Bias/fairness assessments across groups address fairness.

**Q8 — B. Content Understanding.** One multimodal service for docs/images + audio.

**Q9 — B.** max_tokens = length; temperature = randomness.

**Q10 — A & C.** Transcribe = STT; read aloud = TTS.

**Q11 — C. Deployment name.**

**Q12 — A. Content filter (Content Safety).**

**Q13 — A & C.** Embeddings = text→vectors; similar meanings → nearby vectors.

**Q14 — B.** Rewriting a paragraph is a single completion; the others need tools/actions (agent).

**Q15 — A (Yes/No/Yes).** LLMs predict tokens (not DB lookups); grounding reduces hallucination.

**Q16 — B. PTU.** Reserved throughput for predictable latency/SLA.

**Q17 — C.** system = persona/rules/grounding; user = request.

**Q18 — B.** Image-generation model creates images from text.

**Q19 — B.** Content Understanding = multimodal structured extraction via analyzers/field schemas.

**Q20 — B (~0).** Low temperature = stable, non-creative output for extraction.

**Q21 — A & C.** Deploying/interacting in the portal and creating/testing a single agent are Implement-domain skills. The other two are Domain-1 (Identify) concepts.

**Q22 — B. RAG.** Retrieve relevant chunks and add to the prompt; don't paste 400 pages.

**Q23 — B.** Testing for safe behaviour under unexpected inputs = reliability & safety.

**Q24 — B. user.** The image is attached inside the **user** message content.

**Q25 — B. LUIS & QnA Maker** (→ CLU & custom question answering).

**Q26 — B.** A field schema lists the fields Content Understanding extracts.

**Q27 — B.** Agent = instructions + tools + action; multimodal = image/audio understanding; combinable.

**Q28 — B. Embeddings + vector similarity** enable semantic search.

**Q29 — B. Privacy & security.**

**Q30 — A. Stop sequence.**

**Q31 — A & C.** Embeddings and multimodal are model types. Field schema and content filter are not models.

**Q32 — B. Object detection** (detect AND locate each defect).

**Q33 — A.** Prompt shields + a strict system message reduce injection risk.

**Q34 — B.** A single agent needs a model deployment + instructions (tools optional).

**Q35 — B.** Global Standard routes pay-go traffic globally for availability. (Batch ≠ real-time; PTU is reserved not per-token; serverless is managed.)

**Q36 — B.** Chain-of-thought prompting and/or a reasoning model surface step-by-step reasoning.

**Q37 — A (Yes/Yes/No).** Video: yes; field schema: yes; only real-time chat: no.

**Q38 — B.** Create project → deploy model → call it (portal or SDK).

**Q39 — B. Transparency; a transparency note / disclosure.**

**Q40 — B.** The core shift: implement solutions in **Microsoft Foundry** (models, agents, Content Understanding) with basic coding.

---
### Score bands
- **34–40:** ready. - **28–33:** pass-likely. - **<28:** re-drill Modules 02, 05, 06, 07 and Test 1 misses.

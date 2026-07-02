# Practice Test 1 — HARD (AI-901)
**40 questions · scenario-based · exam-authentic.** Recommended time: 45 min. Pass ≈ 28/40.
Answer key + explanations at the bottom. No peeking — these are written to punish guessing.

---

## Questions

**Q1.** A hospital deploys an AI triage assistant. An independent ethics board reviews its decisions and remains answerable for outcomes. Which responsible-AI principle does this MOST directly reflect?
A. Reliability & safety  B. Transparency  C. Accountability  D. Fairness

**Q2.** A generative model confidently states a non-existent court case as precedent. Which technique BEST reduces this behaviour?
A. Increase temperature  B. Grounding / RAG with authoritative sources  C. Raise max_tokens  D. Add a presence penalty

**Q3.** You need output that is as **deterministic and repeatable** as possible for an extraction task. Which two settings help MOST? (Choose TWO)
A. temperature = 0  B. temperature = 1.5  C. a fixed seed  D. presence_penalty = 2

**Q4.** Which task is BEST solved by an **image-generation** model rather than a multimodal (vision) model?
A. Reading the text on a scanned receipt  B. Producing a new poster from a text description  C. Counting people in a photo  D. Describing a chart image

**Q5.** In an AI-901 chat request, where should the rule "Only answer using the provided policy document; refuse anything else" be placed?
A. In the user message  B. In the system message  C. As a stop sequence  D. In the assistant message

**Q6.** A team must extract `vendor`, `invoice_date`, and `total` as **structured fields** from 50,000 scanned invoices in a repeatable pipeline. Which is the BEST fit?
A. Prompt a multimodal model per file, ad hoc  B. Azure Content Understanding with a field schema  C. Speech-to-text  D. Image classification

**Q7.** Which statement about **tokens** is correct?
A. A token always equals one word  B. Tokens are only used for images  C. Model limits and billing are measured in tokens  D. Tokens are the model's random seed

**Q8.** You call a deployed model with the SDK. What value must you pass as `model=`?
A. The base model family name  B. The Azure region  C. The **deployment name** you chose  D. The hub name

**Q9.** Which scenario requires an **agent** rather than a single chat completion?
A. Summarize a paragraph  B. Translate one sentence  C. Look up a customer's order via an API tool, then email a status update  D. Classify a review's sentiment

**Q10.** A voice assistant must **hear** a spoken question and **reply** — using as few moving parts as possible. Which approach aligns with AI-901?
A. A multimodal model that accepts audio input  B. Image classification  C. An embeddings model  D. Object detection

**Q11.** Which pairing correctly matches capability to output?
A. Object detection → single whole-image label  B. Image classification → bounding boxes  C. Speech synthesis → text from audio  D. Speech recognition → text from audio

**Q12.** A model must handle **steady, high-volume production traffic with predictable latency**. Which deployment type fits BEST?
A. Batch  B. Standard  C. Provisioned Throughput (PTU)  D. Serverless free tier

**Q13.** You want the model to consider **fewer, more-likely** word choices without touching temperature. Which parameter do you lower?
A. max_tokens  B. top_p  C. frequency_penalty  D. presence_penalty

**Q14.** Which is a correct description of **embeddings**?
A. Numeric vectors capturing meaning, used for search/similarity  B. A way to cap response length  C. A responsible-AI principle  D. The agent's tool list

**Q15.** A captioning feature must **describe an existing uploaded photo** for accessibility. Which model type?
A. Image-generation model  B. Embeddings model  C. Multimodal (vision) model  D. Speech model

**Q16.** Which two are **text-analysis techniques** explicitly listed for AI-901? (Choose TWO)
A. Sentiment analysis  B. Object detection  C. Summarization  D. Speech synthesis

**Q17.** In the Foundry Agent Service, what does a **run** do?
A. Stores the conversation history only  B. Executes the agent over a thread, possibly calling tools, then produces a response  C. Deploys the base model  D. Sets the content filter

**Q18.** Which responsible-AI principle is MOST associated with providing **captions and screen-reader support** so people with disabilities can use the solution?
A. Inclusiveness  B. Accountability  C. Privacy & security  D. Reliability & safety

**Q19.** You must reduce **repeated phrases** in a model's long output. Which parameter helps?
A. temperature  B. frequency_penalty  C. max_tokens  D. seed

**Q20.** Which of the following is the correct **agent lifecycle** order in the Foundry SDK?
A. thread → run → agent → message  B. agent → thread → message → run → read messages  C. message → agent → run → thread  D. run → message → thread → agent

**Q21.** A dev wants to build a chat client in Python against a Foundry deployment. Which is a valid combination?
A. `azure-identity` only, no client  B. `openai` `AzureOpenAI` client with endpoint, credential, and deployment name  C. Content Understanding analyzer  D. Speech SDK TTS voice

**Q22.** Which scenario is BEST handled by a **reasoning (o-series)** model?
A. High-volume simple FAQ replies  B. Multi-step logic/math word problem requiring careful stepwise reasoning  C. Generating an image  D. Converting text to speech

**Q23.** Which statement about **Content Understanding vs prompting a multimodal model** is TRUE?
A. They are identical  B. Content Understanding is best for consistent structured extraction across many files; a multimodal prompt is best for one-off, flexible questions  C. A multimodal prompt can process video but Content Understanding cannot  D. Content Understanding only works on audio

**Q24.** An AI feature must **not** disadvantage applicants based on gender. This is a consideration for which principle?
A. Transparency  B. Fairness  C. Reliability & safety  D. Inclusiveness

**Q25.** Which two objects define the **structure** inside Microsoft Foundry? (Choose TWO)
A. Hub  B. Analyzer  C. Project  D. Stop sequence

**Q26.** A support team wants **action items and sentiment** extracted from thousands of recorded calls. Best fit?
A. Image classification  B. Content Understanding (audio)  C. DALL·E  D. Object detection

**Q27.** Which is TRUE about a chat model's "memory"?
A. The model persists all prior chats server-side automatically  B. The app must resend prior messages each call; the model is stateless per request  C. Temperature stores memory  D. Embeddings store the chat history

**Q28.** Which parameter primarily controls **response length**?
A. temperature  B. top_p  C. max_tokens  D. frequency_penalty

**Q29.** A model must classify whether an X-ray shows "fracture / no fracture" — one label for the whole image. This is:
A. Object detection  B. Image classification  C. Image generation  D. OCR

**Q30.** Which is the BEST example of **grounding** a generative model?
A. Raising temperature to 2  B. Injecting retrieved company policy text into the prompt so answers use it  C. Adding a stop sequence  D. Using a larger max_tokens

**Q31.** Which two are valid ways to **authenticate** to a Foundry model call? (Choose TWO)
A. API key + endpoint  B. Microsoft Entra ID via DefaultAzureCredential  C. The model's temperature  D. A bounding box

**Q32.** A prompt-injection attack tries to make the model ignore its rules. Which Foundry capability defends against this?
A. Prompt shields  B. Higher temperature  C. Batch deployment  D. Embeddings

**Q33.** Which task should use an **embeddings** model?
A. Generating a summary  B. Building semantic search over documents  C. Reading text aloud  D. Creating an image

**Q34.** Which correctly distinguishes **speech recognition** from **speech synthesis**?
A. Recognition = text→audio; synthesis = audio→text  B. Recognition = audio→text; synthesis = text→audio  C. Both convert text to text  D. Both are image tasks

**Q35.** In the Foundry portal, you enable a **file-search** tool on an assistant and upload PDFs. You are configuring:
A. A deployment type  B. An agent's tool/knowledge  C. A content filter threshold  D. A speech voice

**Q36.** A retailer wants to auto-generate marketing images and also read text from product photos. Which two model types are needed? (Choose TWO)
A. Image-generation model  B. Multimodal (vision) model  C. Embeddings model only  D. Speech model

**Q37.** Which is a correct statement about **model selection**?
A. Always use the largest model regardless of cost/latency  B. Choose based on capability/modality, cost, latency, and context window  C. Only reasoning models can do chat  D. Small models cannot run in Foundry

**Q38.** A company must **disclose to users that they are chatting with an AI** and explain its limitations. Which principle?
A. Accountability  B. Transparency  C. Privacy & security  D. Fairness

**Q39.** Which best describes the difference between the **Foundry portal** and the **Foundry SDK**?
A. They do unrelated things  B. Portal = build/deploy/test in the browser (no code); SDK = do the same from code  C. The SDK cannot call deployed models  D. The portal cannot deploy models

**Q40.** You must extract structured fields from **documents, images, AND video** with one consistent approach. Which service?
A. Azure AI Translator  B. Azure Content Understanding  C. Azure AI Speech  D. Custom Vision

---

## Answer Key & Explanations

**Q1 — C. Accountability.** People/orgs being *answerable* + governance/oversight = accountability. Reliability & safety is about the *system* behaving correctly, not who answers for it.

**Q2 — B. Grounding / RAG.** Hallucinations come from the model predicting plausible tokens without facts; supplying authoritative retrieved data grounds answers. Temperature/max_tokens/penalties don't add facts.

**Q3 — A & C.** temperature=0 (minimal randomness) and a fixed **seed** maximize repeatability. High temperature or presence_penalty add variability.

**Q4 — B.** Image-generation models *create* new images from text. Reading/counting/describing existing images are **multimodal (vision)** tasks.

**Q5 — B. System message.** Rules, persona, grounding, and refusals belong in the **system** message. Putting them in the user message is the classic distractor.

**Q6 — B. Content Understanding with a field schema.** Structured, repeatable, high-volume extraction is exactly its purpose. Ad-hoc per-file prompting isn't consistent/scalable.

**Q7 — C.** Limits and billing are token-based. A token is *roughly* a word-piece, not exactly one word, and isn't image-only or a seed.

**Q8 — C. The deployment name.** Code references the deployment name you created, not the base family, region, or hub.

**Q9 — C.** Looking up data via a tool then taking an action (email) is multi-step, tool-using = **agent**. The others are single text-in/text-out completions.

**Q10 — A.** A multimodal model accepting **audio** can hear and respond with minimal plumbing. Embeddings/object detection are unrelated.

**Q11 — D.** Speech recognition = audio→text. Detection gives boxes; classification gives a label; synthesis = text→audio.

**Q12 — C. Provisioned Throughput (PTU).** Reserved capacity gives predictable latency for steady high volume. Batch is async bulk; Standard is pay-go without reserved capacity.

**Q13 — B. top_p.** Nucleus sampling; lowering it restricts to the most probable tokens without changing temperature.

**Q14 — A.** Embeddings are meaning vectors for search/similarity/RAG.

**Q15 — C. Multimodal (vision) model.** Describing an existing image = vision understanding, not generation.

**Q16 — A & C.** Sentiment analysis and summarization are named text-analysis techniques (also keyword extraction, entity detection). Object detection/speech synthesis are other workloads.

**Q17 — B.** A run executes the agent over a thread, may invoke tools, then returns a response. Threads store history; deployments handle the model.

**Q18 — A. Inclusiveness.** Empowering people of all abilities/backgrounds (accessibility) = inclusiveness.

**Q19 — B. frequency_penalty.** Discourages repeating frequent tokens. Temperature adds randomness generally; max_tokens caps length; seed aids reproducibility.

**Q20 — B.** create agent → create thread → add message → create/process run → read messages.

**Q21 — B.** A valid chat client uses an SDK client (e.g., `AzureOpenAI`) with endpoint + credential + deployment name.

**Q22 — B.** Reasoning (o-series) models excel at careful multi-step logic/math. High-volume simple replies suit small models; images/TTS need other model types.

**Q23 — B.** Content Understanding = consistent structured extraction across many files/modalities; a multimodal prompt = flexible one-off answers. Both can address video/audio depending on modality, but the *distinction* is structured-vs-adhoc.

**Q24 — B. Fairness.** Not disadvantaging by gender = mitigating bias = fairness.

**Q25 — A & C.** Hub and Project are Foundry's workspace structure. Analyzer belongs to Content Understanding; stop sequence is an inference parameter.

**Q26 — B. Content Understanding (audio).** Structured extraction (action items, sentiment) from many recordings.

**Q27 — B.** Chat models are stateless per request; the app resends prior messages to maintain context.

**Q28 — C. max_tokens.** Directly caps output length. Temperature/top_p affect randomness; frequency_penalty affects repetition.

**Q29 — B. Image classification.** One whole-image label = classification (detection would add location/boxes).

**Q30 — B.** Grounding = supplying the model with retrieved authoritative content to base answers on.

**Q31 — A & B.** API key+endpoint, or Microsoft Entra ID via DefaultAzureCredential.

**Q32 — A. Prompt shields.** Defends against prompt-injection/jailbreak. Temperature/batch/embeddings are irrelevant to that defense.

**Q33 — B.** Embeddings power semantic/similarity search.

**Q34 — B.** Recognition = audio→text (STT); synthesis = text→audio (TTS).

**Q35 — B.** Uploading files + enabling file search configures an **agent's tool/knowledge**.

**Q36 — A & B.** Generate marketing images → image-generation model; read text from photos → multimodal (vision) model.

**Q37 — B.** Model selection weighs capability/modality, cost, latency, and context window — not "always biggest."

**Q38 — B. Transparency.** Disclosing it's AI and stating limitations = transparency.

**Q39 — B.** Portal = no-code build/deploy/test; SDK = same capabilities from code.

**Q40 — B. Azure Content Understanding.** One multimodal service for documents, images, audio, and video extraction.

---
### Score bands
- **34–40:** exam-ready. - **28–33:** pass-likely; review misses. - **21–27:** revisit Modules 02, 06, 07. - **<21:** re-study the whole kit before Test 2.

# FULL EXAM SIMULATION — AI-901
**50 questions · 60 minutes · closed book.** Weighted like the real exam:
Domain 1 "Identify AI concepts & capabilities" ≈ **22 Q (40–45%)** · Domain 2 "Implement with Foundry" ≈ **28 Q (55–60%)**.
Passing ≈ **35/50 (700-scaled)**. Administer timed, then review **every** answer.

> **Proctoring tip:** enforce 60 min, no notes. Simulate the sandbox at `aka.ms/examdemo` beforehand so nobody loses time to the UI.

---

## SECTION 1 — Identify AI concepts & capabilities (Q1–Q22)

**Q1.** A governance committee is accountable for an AI system's decisions and maintains an audit trail. Which principle?
A. Transparency  B. Accountability  C. Reliability & safety  D. Inclusiveness

**Q2.** Which is the correct definition of a **token**?
A. A user's API key  B. The unit of text a model processes; limits/billing are token-based  C. A responsible-AI principle  D. A deployment type

**Q3.** An assistant must **create** original images from text prompts. Which model type?
A. Multimodal (vision)  B. Embeddings  C. Image-generation  D. Speech

**Q4.** Which parameter most directly makes output **more focused and less random**?
A. Raise temperature  B. Lower temperature  C. Raise max_tokens  D. Raise presence_penalty

**Q5.** A solution adds **captions and alt-text** so people with hearing/visual impairments can use it. Principle?
A. Inclusiveness  B. Fairness  C. Privacy & security  D. Accountability

**Q6.** Which task needs an **agent** (not a single completion)?
A. Translate a sentence  B. Summarize a review  C. Query an inventory API and place a reorder  D. Detect sentiment

**Q7.** Which two are **text-analysis** techniques? (Choose TWO)
A. Entity detection  B. Image classification  C. Keyword extraction  D. Speech synthesis

**Q8.** "Predict next month's revenue as a number" is which ML task?
A. Classification  B. Clustering  C. Regression  D. Object detection

**Q9.** Which BEST reduces **hallucinations**?
A. Grounding the model with retrieved authoritative data  B. Increasing temperature  C. Removing the system message  D. Using a larger max_tokens

**Q10.** Speech-to-text is:
A. Speech synthesis  B. Speech recognition  C. Translation  D. Summarization

**Q11.** Which model type turns text into **vectors** for semantic search?
A. Image-generation  B. Embeddings  C. Reasoning  D. Speech

**Q12.** A self-driving feature is rigorously tested to behave safely in rare conditions. Principle?
A. Reliability & safety  B. Fairness  C. Transparency  D. Privacy & security

**Q13.** Which is TRUE about multimodal models?
A. They only output images  B. They can accept inputs beyond text, e.g., images/audio  C. They cannot do chat  D. They are the same as embeddings

**Q14.** A tricky multi-step math/logic problem is best handled by a:
A. Small model at temperature 2  B. Reasoning (o-series) model  C. Image model  D. Embeddings model

**Q15.** Which parameter caps the **length** of a response?
A. temperature  B. top_p  C. max_tokens  D. seed

**Q16.** "Group customers into segments with no predefined labels" is:
A. Classification  B. Clustering  C. Regression  D. NER

**Q17.** Which is a consideration for **privacy & security**?
A. Publishing a fairness dashboard  B. De-identifying personal data and securing the model  C. Adding captions  D. Disclosing that it's AI

**Q18.** Which output does **object detection** produce that classification does not?
A. A caption  B. Bounding boxes / locations  C. A transcript  D. An embedding

**Q19.** A company selects a model by weighing capability, **cost, latency, and context window**. This is:
A. Prompt engineering  B. Model selection  C. Grounding  D. Fine-tuning

**Q20.** Which technique disambiguates whether "Amazon" means the river or the company?
A. Sentiment analysis  B. Entity linking  C. Summarization  D. Speech synthesis

**Q21.** Which statement about **generative models** is TRUE?
A. They retrieve exact answers from a database  B. They predict likely tokens from learned patterns  C. They cannot be grounded  D. They require object detection

**Q22.** A chatbot must **disclose to users that it is AI** and note its limitations. Principle?
A. Accountability  B. Transparency  C. Fairness  D. Inclusiveness

---

## SECTION 2 — Implement AI solutions using Microsoft Foundry (Q23–Q50)

**Q23.** In code, the `model=` argument passed to a chat completion is the:
A. Base model family  B. Deployment name  C. Region  D. Hub name

**Q24.** Where do persona, rules, and grounding belong in a chat request?
A. user message  B. system message  C. stop sequence  D. assistant message

**Q25.** Which is the correct **agent** definition?
A. A deployment type  B. Model + instructions + tools (+ knowledge) that can act  C. A field schema  D. A content filter

**Q26.** Correct **agent lifecycle** order?
A. run → thread → agent → message  B. agent → thread → message → run → read messages  C. thread → message → agent  D. message → run → agent → thread

**Q27.** You need structured extraction of `total`, `date`, `vendor` from thousands of receipts. Use:
A. Prompt a multimodal model ad hoc  B. Content Understanding with a field schema  C. Embeddings  D. Speech recognition

**Q28.** (Multi-select) Two valid ways to authenticate a Foundry call? (Choose TWO)
A. API key + endpoint  B. temperature  C. Microsoft Entra ID (DefaultAzureCredential)  D. bounding box

**Q29.** **Complete the code:**
```python
resp = client.chat.completions.create(model="gpt-4o-mini",
    messages=[{"role":"system","content":"Be concise."},
              {"role":"____","content":"Explain RAG."}])
```
A. tool  B. user  C. deployment  D. filter

**Q30.** Which Foundry object is the **top-level** collaborative workspace containing projects?
A. Deployment  B. Hub  C. Analyzer  D. Thread

**Q31.** A deployment must handle steady heavy production load with predictable latency. Choose:
A. Batch  B. Provisioned Throughput (PTU)  C. Free tier  D. Serverless spot

**Q32.** To let an agent answer from your uploaded PDFs, you add which tool?
A. File search / knowledge  B. Image generation  C. Speech voice  D. Higher temperature

**Q33.** You want the model to **stop** at `<END>`. Configure:
A. stop sequence  B. temperature  C. seed  D. top_p

**Q34.** Which BEST describes the **Foundry portal** vs **Foundry SDK**?
A. Unrelated tools  B. Portal = no-code build/deploy/test; SDK = same from code  C. SDK cannot call models  D. Portal cannot deploy

**Q35.** A voice bot must **hear** audio and reply with minimal plumbing. Use:
A. Object detection  B. A multimodal model that accepts audio  C. Embeddings  D. Image generation

**Q36.** (Multi-select) Two things you configure when **deploying** a model? (Choose TWO)
A. Deployment name  B. Deployment type (Standard/PTU/etc.)  C. The user's question  D. The agent's thread

**Q37.** To read chatbot answers **aloud**, use:
A. Speech recognition  B. Speech synthesis  C. Content Understanding video  D. Object detection

**Q38.** A field schema in Content Understanding defines:
A. Temperature  B. The specific fields to extract  C. The agent's model  D. The hub

**Q39.** Which reduces **prompt-injection** risk?
A. Prompt shields + strict system message  B. Raising temperature  C. Larger max_tokens  D. Batch deployment

**Q40.** For an extraction task requiring stable output, set temperature to:
A. ~0  B. 1.0  C. 2.0  D. Irrelevant

**Q41.** Which is TRUE about chat memory?
A. The model stores all history server-side automatically  B. The client resends prior messages; the model is stateless per call  C. Embeddings hold the chat  D. max_tokens stores memory

**Q42.** To interpret an uploaded photo in a prompt, the image is placed in the ___ message content:
A. system  B. user  C. assistant  D. tool

**Q43.** Which Foundry feature measures app quality (groundedness, relevance, safety)?
A. Evaluations  B. Hubs  C. Stop sequences  D. Batch

**Q44.** Which single service extracts structured info from **documents, images, audio, and video**?
A. Translator  B. Azure Content Understanding  C. Speech only  D. Custom Vision

**Q45.** A support solution should **retrieve** relevant KB chunks and add them to the prompt. This is:
A. Fine-tuning  B. RAG / grounding  C. Object detection  D. Image generation

**Q46.** (Multi-select) Two are **inference parameters**? (Choose TWO)
A. frequency_penalty  B. Hub  C. top_p  D. Analyzer

**Q47.** To generate marketing images from text briefs, deploy a:
A. Reasoning model  B. Image-generation model (DALL·E/GPT-image)  C. Embeddings model  D. Speech model

**Q48.** The minimum to create & test a **single agent** in the portal:
A. Only a hub  B. A model deployment + instructions (tools optional)  C. A field schema  D. A translator resource

**Q49.** Which correctly matches deployment type to use?
A. Batch → real-time chat  B. Global Standard → pay-go routed for availability  C. PTU → per-token no reservation  D. Serverless → you manage VMs

**Q50.** Which best summarizes what AI-901 assesses?
A. Only ML math  B. Identifying AI concepts + implementing solutions in Microsoft Foundry (models, agents, Content Understanding) with basic coding  C. Only computer vision  D. Only Azure administration

---

## ANSWER KEY

| Q | A | Q | A | Q | A | Q | A | Q | A |
|---|---|---|---|---|---|---|---|---|---|
| 1 | B | 11 | B | 21 | B | 31 | B | 41 | B |
| 2 | B | 12 | A | 22 | B | 32 | A | 42 | B |
| 3 | C | 13 | B | 23 | B | 33 | A | 43 | A |
| 4 | B | 14 | B | 24 | B | 34 | B | 44 | B |
| 5 | A | 15 | C | 25 | B | 35 | B | 45 | B |
| 6 | C | 16 | B | 26 | B | 36 | A,B | 46 | A,C |
| 7 | A,C | 17 | B | 27 | B | 37 | B | 47 | B |
| 8 | C | 18 | B | 28 | A,C | 38 | B | 48 | B |
| 9 | A | 19 | B | 29 | B | 39 | A | 49 | B |
| 10 | B | 20 | B | 30 | B | 40 | A | 50 | B |

### One-line rationales for the trickiest
- **Q6/Q25/Q26/Q48:** anything requiring **actions/tools/multi-step** = **agent**; lifecycle = agent→thread→message→run→read.
- **Q9/Q45:** hallucination fix = **grounding/RAG** (retrieve then add to prompt).
- **Q4/Q15/Q40:** temperature = randomness (lower = focused); **max_tokens = length**.
- **Q27/Q38/Q44:** structured, multimodal extraction = **Content Understanding** with a **field schema**.
- **Q23/Q29/Q42/Q24:** code references the **deployment name**; **user** message carries the request/image; **system** carries rules/grounding.
- **Q31/Q49:** **PTU** = reserved predictable latency; **Global Standard** = pay-go routed for availability; **Batch** = async bulk.
- **Q3/Q47 vs Q13/Q35/Q42:** **image-generation** *creates* images; **multimodal** *understands* images/audio.

### Score → verdict
- **43–50:** strong pass, book the exam. - **35–42:** pass-likely; review misses + Module 12. - **28–34:** borderline; re-drill Modules 06–07 and both practice tests. - **<28:** not ready — repeat the kit.

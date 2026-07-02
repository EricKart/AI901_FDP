# Module 05 — Speech & Information Extraction (Azure Content Understanding)
### Day 4 · Session 2 | Domain 1 (speech + info-extraction concepts) + Domain 2 (implement in Foundry)

> **Biggest change from AI-900:** "Document Intelligence / Form Recognizer / Video Indexer" as separate products are **out**. AI-901 uses **Azure Content Understanding** — one multimodal service to extract structured info from **documents, images, audio, and video** — accessed via **Foundry Tools**.

---

## PART A — Speech (Domain 1 concepts)

Two core capabilities the exam names — keep them straight:

| Capability | Direction | Also called | Scenario |
|---|---|---|---|
| **Speech recognition** | **Speech → text** | Speech-to-text (STT), transcription | Transcribe a meeting, voice commands, captions |
| **Speech synthesis** | **Text → speech** | Text-to-speech (TTS) | Read content aloud, voice responses, IVR |

Related: **speech translation** (spoken input → translated text/speech), **speaker recognition** (identify/verify a speaker), **neural voices** & **SSML** (control pronunciation, pitch, rate, pauses in TTS).

> **Exam trap:** *"transcribe a recording"* → **speech recognition (STT)**. *"read the answer out loud"* → **speech synthesis (TTS)**. *"translate a spoken Spanish sentence into English audio"* → **speech translation**.

### Two ways speech shows up in AI-901 implementation
1. **Azure Speech in Foundry Tools** — the dedicated speech service (STT/TTS) surfaced as a Foundry tool; build a lightweight app that transcribes or speaks.
2. **Respond to spoken prompts with a multimodal model** — a multimodal model (e.g., GPT-4o audio/realtime) can take **audio in** and respond, enabling voice conversations without wiring STT+LLM+TTS manually.

---

## PART B — Information extraction with Azure Content Understanding (Domain 1 + 2) ⭐

### What Content Understanding is
**Azure Content Understanding** is a Foundry service that turns **unstructured content into structured data** across **four modalities**:
- **Documents & forms** (PDFs, scans) — invoices, receipts, contracts, IDs, tables, key/value fields.
- **Images** — extract fields/attributes from pictures, diagrams, screenshots.
- **Audio** — transcribe + extract fields from calls (e.g., topics, sentiment, action items).
- **Video** — segment, transcribe, and extract scenes/entities/summaries.

It uses **generative models** under the hood, so you can define **exactly the fields you want** in plain language.

### The key concept: the **analyzer** + **field schema**
- You create an **analyzer** and define a **field schema** — the list of fields to extract (e.g., `vendor_name`, `invoice_date`, `total_amount`, `line_items[]`).
- You can start from a **prebuilt analyzer** (e.g., invoice/receipt/call-recording) or build a **custom** one.
- You submit a file; it returns **structured JSON** matching your schema, with values and confidence.

> **Exam framing:** *"Extract the vendor, date, and total from thousands of scanned invoices as structured data"* → **Content Understanding** (define a field schema, run the analyzer). *"Summarize and pull action items from support-call recordings"* → **Content Understanding (audio)**. *"Answer one ad-hoc question about a single photo"* → that's better as **prompt a multimodal model** (Module 03).

### Content Understanding vs prompting a multimodal model (critical distinction)
| Use **Content Understanding** when… | Use **a multimodal model prompt** when… |
|---|---|
| You need **consistent, structured** fields (a schema) | You need a **one-off, flexible** answer about content |
| **Batch / many files**, repeatable pipeline | Ad-hoc reasoning over a single item |
| Across documents/images/audio/video with defined outputs | Conversational Q&A about an image/audio |

### Implementing it (Foundry Tools) — illustrative flow
```text
1. In Foundry → Tools → Content Understanding, create an analyzer.
2. Define the field schema (the fields you want extracted).
3. (Optional) Add a few sample files to improve extraction.
4. Run the analyzer on a file → receive structured JSON.
5. Call it from an app via SDK/REST for a "lightweight extraction app".
```
```python
# Illustrative: call a Content Understanding analyzer over REST/SDK
# (exact SDK surface evolves — teach the shape, not memorized syntax)
result = content_understanding_client.analyze(
    analyzer_id="invoice-analyzer",
    file_url="https://example.com/invoice001.pdf",
)
for field, value in result.fields.items():
    print(field, "=", value)
```

---

## C. Session 2 live-demo checklist
1. **Azure Speech in Foundry**: transcribe a short audio clip (STT), then synthesize a sentence to audio (TTS); tweak a neural voice.
2. Show a **multimodal model** answering a **spoken** prompt (audio in → answer).
3. **Content Understanding**: create an **invoice analyzer**, define fields (vendor, date, total), run it on a sample invoice, show the structured JSON.
4. Run the analyzer on a **call recording** to show audio extraction (transcript + fields).
5. Contrast: ask a multimodal model one ad-hoc question about the same invoice → discuss "structured pipeline vs one-off answer."

## D. Scenario drill
| Scenario | Answer |
|---|---|
| Transcribe recorded interviews | **Speech recognition (STT)** |
| Read chatbot answers aloud | **Speech synthesis (TTS)** |
| Voice assistant that hears and replies with one model | **Multimodal model (audio)** |
| Extract vendor/date/total from 10,000 invoices → structured data | **Content Understanding (documents)** |
| Pull action items + sentiment from support calls | **Content Understanding (audio)** |
| Summarize and index a video library | **Content Understanding (video)** |
| Ask one question about a single scanned page | **Prompt a multimodal model** |

## E. Rapid recall
1. Speech-to-text vs text-to-speech — which is recognition, which is synthesis? *(STT = recognition; TTS = synthesis)*
2. One service to extract structured info from docs/images/audio/video? *(Azure Content Understanding)*
3. What do you define to tell Content Understanding which fields to pull? *(a field schema / analyzer)*
4. Batch structured extraction → Content Understanding; one-off ad-hoc question → ? *(prompt a multimodal model)*
5. Which two products did Content Understanding effectively replace on the exam? *(Document Intelligence/Form Recognizer + Video Indexer)*

# AI-901 FDP — Diagram Pack (Mermaid)

All diagrams render automatically on GitHub and are embedded in the interactive slides. Use them as whiteboard references while teaching.

---

## 1. Course map — how everything connects
```mermaid
mindmap
  root((AI-901<br/>Azure AI Fundamentals))
    Domain 1 (40-45%)<br/>Identify concepts
      Responsible AI
        Fairness
        Reliability & Safety
        Privacy & Security
        Inclusiveness
        Transparency
        Accountability
      How GenAI works
        Tokens & Embeddings
        Transformers
        Model selection
        Deployment & config
      AI workloads
        Generative & Agentic
        Text analysis
        Speech
        Computer vision
        Information extraction
    Domain 2 (55-60%)<br/>Implement in Foundry
      Foundry portal & endpoints
      Deploy & prompt a model
      Foundry SDK chat client
      Agents (model+instructions+tools)
      Text & Speech in Foundry Tools
      Vision & image/video generation
      Content Understanding
```

---

## 2. Exam blueprint — weightings
```mermaid
pie showData
    title AI-901 exam weighting
    "Identify AI concepts & capabilities" : 42
    "Implement AI solutions with Microsoft Foundry" : 58
```

---

## 3. Microsoft Foundry architecture
```mermaid
flowchart TD
    A["Microsoft Foundry (ai.azure.com)"] --> B[Hub]
    B --> C[Project]
    C --> D[Model Catalog]
    D -->|deploy| E["Deployment<br/>(deployment name + endpoint + content filter)"]
    C --> F["Tools"]
    F --> F1[Azure Speech]
    F --> F2[Content Understanding]
    F --> F3["Grounding / Search"]
    C --> G["Agents<br/>(model + instructions + tools)"]
    E --> H["Endpoint"]
    H --> I["Your app<br/>Foundry SDK / REST"]
    G --> I
    I --> J["Auth: API key OR Microsoft Entra ID"]
```

---

## 4. Workload decision tree — scenario → capability
```mermaid
flowchart TD
    S([What does the scenario need?]) --> Q1{Create new content?}
    Q1 -->|Yes, text| T[Generative chat model]
    Q1 -->|Yes, still image| IG[Image-generation model]
    Q1 -->|Yes, video| VG[Video-generation model]
    Q1 -->|No| Q2{Act with tools / multi-step?}
    Q2 -->|Yes| AG[Agent]
    Q2 -->|No| Q3{What modality?}
    Q3 -->|Understand an image/audio| MM[Multimodal model]
    Q3 -->|Speech to text| STT[Speech recognition]
    Q3 -->|Text to speech| TTS[Speech synthesis]
    Q3 -->|Analyze text| TA["Text analysis<br/>sentiment / entities / keywords / summary"]
    Q3 -->|Extract structured fields from files| CU["Content Understanding<br/>(docs / images / audio / video)"]
    Q3 -->|Predict number / category / group| ML["Machine learning<br/>regression / classification / clustering"]
```

---

## 5. Model selection & inference config
```mermaid
flowchart LR
    subgraph Pick a model
      R[Reasoning o-series<br/>complex logic] 
      SMc[Small model<br/>cheap/fast/high volume]
      MMc[Multimodal<br/>image/audio in]
      IMc[Image-gen]
      EMc[Embeddings<br/>search/RAG]
    end
    subgraph Deployment type
      Std[Standard]
      GS[Global Standard]
      PTU[Provisioned / PTU]
      Bat[Batch]
      SL[Serverless / MaaS]
    end
    subgraph Inference params
      TEMP["temperature / top_p = randomness"]
      MAXT["max_tokens = length"]
      FP["frequency / presence penalty = repetition / novelty"]
      SEED["seed = reproducible"]
      STOP["stop = halt token"]
    end
```

---

## 6. Agent lifecycle (Foundry Agent Service)
```mermaid
sequenceDiagram
    participant Dev as Your app (SDK)
    participant AG as Agent (model+instructions+tools)
    participant TH as Thread
    participant TL as Tool (file search / function / code)
    Dev->>AG: 1. create_agent(model, instructions, tools)
    Dev->>TH: 2. create_thread()
    Dev->>TH: 3. create_message(role="user", content=...)
    Dev->>AG: 4. create_and_process_run(thread, agent)
    AG->>TL: (may call a tool)
    TL-->>AG: tool result
    AG-->>TH: assistant message
    Dev->>TH: 5. list_messages() -> read reply
```

---

## 7. Chat request anatomy
```mermaid
flowchart LR
    subgraph Request["messages = [ ... ]"]
      SY["system:<br/>persona, rules, grounding, format"]
      US["user:<br/>the actual request (+ image/audio)"]
      AS["assistant:<br/>prior replies (context)"]
    end
    Request --> M["Deployed model<br/>(deployment name)"]
    M --> OUT["response.choices[0].message.content"]
```

---

## 8. Content Understanding flow
```mermaid
flowchart LR
    F["Input file<br/>document / image / audio / video"] --> AN["Analyzer"]
    SC["Field schema<br/>(vendor, date, total, ...)"] --> AN
    AN --> JS["Structured JSON<br/>field = value (+ confidence)"]
    JS --> APP["Lightweight extraction app"]
```

---

## 9. Responsible AI — anchor map (FRITAP)
```mermaid
flowchart TD
    RAI[Responsible AI] --> F["Fairness<br/>no bias across groups"]
    RAI --> R["Reliability & Safety<br/>system behaves safely"]
    RAI --> I["Inclusiveness<br/>everyone, all abilities"]
    RAI --> T["Transparency<br/>disclose it's AI + limits"]
    RAI --> A["Accountability<br/>people answerable + governance"]
    RAI --> P["Privacy & Security<br/>protect data + secure system"]
    RAI -.gen-AI controls.-> CS["Content Safety filter"]
    RAI -.gen-AI controls.-> PS["Prompt shields"]
    RAI -.gen-AI controls.-> GR["Grounding / RAG vs hallucination"]
```

# AI-901 FDP — Hands-on Labs

Lab-first is the whole point of AI-901. These labs mirror the **exercises in the two official Learning Paths** and give every learner the muscle memory the exam now rewards. Starter code is in [`labs/code/`](code/).

> **Cost control:** use **GPT-4o-mini** and small token limits. **Delete deployments** after class. A student/free Azure subscription is enough.

---

## Lab 0 — Environment setup (do before Day 3)

1. **Azure access** — an Azure subscription (free / Azure for Students / lab tenant) with **Azure OpenAI / Foundry model access** enabled.
2. **Create a Foundry project** — go to **https://ai.azure.com** → *Create project* (a hub is created for you) in a region that offers GPT-4o-mini + an image model.
3. **Local tools**
   ```bash
   python --version          # 3.10+
   pip install -r labs/code/requirements.txt
   ```
4. **Config** — copy `labs/code/.env.example` to `labs/code/.env` and fill in your endpoint + key + deployment name (get these after Lab 1).

**Checkpoint:** `python -c "import openai, azure.ai.projects; print('ok')"` prints `ok`.

---

## Lab 1 — Deploy a model & use it in the portal
*(Path 2 → "Get started with AI in Azure" exercise)*

1. In your project → **Models + endpoints** → **Deploy model** → choose **gpt-4o-mini** → **Deploy**.
2. Note three things: the **deployment name**, the **endpoint** URL, and a **key** (Keys blade).
3. Open **Playground → Chat**. Set a **system message**: *"You are a concise study coach."* Ask a question.
4. Slide **temperature** 0 → 1.5 and resend; then set **max tokens** low and watch truncation.
5. Click **View code** — see the ready-made SDK snippet.

**You learned:** deployment name vs base model, endpoints, system message, temperature vs max_tokens.
**Exam link:** *Deploy a model and interact with it in the Foundry portal.*

---

## Lab 2 — Lightweight chat client with the Foundry SDK
*(Path 2 → "Get started with generative AI and agents")*

1. Fill `labs/code/.env` with the values from Lab 1.
2. Run:
   ```bash
   python labs/code/chat_client.py
   ```
3. Edit the **system message** in the file and rerun — observe the behaviour change.
4. Change `temperature` and `max_tokens`; rerun.

**You learned:** `client.chat.completions.create(model=deployment, messages=[...])` and reading `choices[0].message.content`.
**Exam link:** *Create a lightweight chat client application by using the Foundry SDK.*

---

## Lab 3 — Create & run a single agent
*(Path 2 → "Creating an agent")*

**Portal:** Project → **Agents** → **New agent** → pick your model → instructions: *"You are an AI-901 tutor. Use the attached notes. Be concise."* → add a **file-search** tool and upload a PDF of notes → **Test** in the playground.

**SDK:**
```bash
python labs/code/agent.py
```
Walk the lifecycle printed by the script: **create agent → thread → message → run → read messages**.

**You learned:** agent = model + instructions + tools; a **run** executes tool calls then answers.
**Exam link:** *Create and test a single-agent solution; build a lightweight client application for an agent.*

---

## Lab 4 — Information extraction with Content Understanding
*(Path 2 → "Get started with information extraction")*

1. Project → **Tools → Content Understanding** → **Create analyzer**.
2. Start from the **invoice/receipt** template (or custom) and define a **field schema**: `vendor`, `invoice_date`, `total`, `line_items[]`.
3. Upload a sample invoice → **Run** → inspect the **structured JSON**.
4. Repeat with a **call recording** (audio) or a short **video** to see multimodal extraction.
5. (Optional) call the analyzer from code — see `labs/code/extract_content.py` (template).

**You learned:** analyzer + field schema; one service across documents/images/audio/video.
**Exam link:** *Extract information from documents, images, audio, and video using Azure Content Understanding.*

---

## Lab 5 — Vision, image generation & speech (quick wins)
*(Path 2 → "Get started with computer vision" / "…with speech")*

- **Vision (multimodal):** in the playground, attach a photo to your gpt-4o deployment → *"Describe this and read any text."*
- **Image generation:** deploy **dall-e-3** → generate 2 images from prompts.
- **Speech:** in **Tools → Speech** (or Speech playground), transcribe a short clip (STT) and synthesize a sentence (TTS); try a different neural voice.

**Exam link:** *Interpret visual input with a multimodal model; create visual outputs; build with Azure Speech in Foundry Tools.*

---

## Text-analysis mini-lab (Day 4)
Run `python labs/code/analyze_text.py` — it prompts a model to return **sentiment + key phrases + entities + summary** as JSON at `temperature=0`. Change the input text and observe consistent, structured output.
**Exam link:** *Build a lightweight application that includes text analysis.*

---

## Lab → exam-objective coverage
| Lab | Objective |
|---|---|
| 1 | Deploy & interact with a model in the Foundry portal |
| 2 | Lightweight chat client with the Foundry SDK |
| 3 | Single-agent solution + agent client app |
| 4 | Information extraction with Content Understanding |
| 5 | Multimodal vision, image generation, Azure Speech |
| Text mini | Lightweight text-analysis app |

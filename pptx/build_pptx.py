#!/usr/bin/env python3
"""
Build branded AI-901 FDP PowerPoint decks (one .pptx per day) from structured content.
Run:  python pptx/build_pptx.py     (output .pptx files land in the pptx/ folder)
Requires: python-pptx  (pip install python-pptx)
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# ---- palette (matches the reveal.js theme) ----
BG    = RGBColor(0x0B, 0x10, 0x20)
CARD  = RGBColor(0x16, 0x1F, 0x3D)
INK   = RGBColor(0xE8, 0xEC, 0xF8)
MUTE  = RGBColor(0xA7, 0xB0, 0xC8)
ACC   = RGBColor(0x5B, 0x8C, 0xFF)
ACC2  = RGBColor(0x22, 0xD3, 0xEE)
WARN  = RGBColor(0xF5, 0x9E, 0x0B)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

HERE = os.path.dirname(os.path.abspath(__file__))
EMU_W, EMU_H = Inches(13.333), Inches(7.5)


def new_deck():
    prs = Presentation()
    prs.slide_width = EMU_W
    prs.slide_height = EMU_H
    return prs


def _bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = BG


def _box(slide, l, t, w, h):
    tb = slide.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    return tb, tf


def _accent_bar(slide):
    bar = slide.shapes.add_shape(1, Inches(0), Inches(0), Inches(0.18), EMU_H)
    bar.fill.solid(); bar.fill.fore_color.rgb = ACC
    bar.line.fill.background()


def title_slide(prs, kicker, title, subtitle):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(s); _accent_bar(s)
    _, tf = _box(s, Inches(0.9), Inches(2.1), Inches(11.5), Inches(1))
    p = tf.paragraphs[0]; r = p.add_run(); r.text = kicker
    r.font.size = Pt(18); r.font.bold = True; r.font.color.rgb = ACC2
    _, tf = _box(s, Inches(0.9), Inches(2.7), Inches(11.6), Inches(2.4))
    p = tf.paragraphs[0]; r = p.add_run(); r.text = title
    r.font.size = Pt(46); r.font.bold = True; r.font.color.rgb = WHITE
    _, tf = _box(s, Inches(0.9), Inches(5.0), Inches(11.6), Inches(1))
    p = tf.paragraphs[0]; r = p.add_run(); r.text = subtitle
    r.font.size = Pt(18); r.font.color.rgb = MUTE
    return s


def _title(slide, text):
    _, tf = _box(slide, Inches(0.7), Inches(0.45), Inches(12), Inches(1))
    p = tf.paragraphs[0]; r = p.add_run(); r.text = text
    r.font.size = Pt(32); r.font.bold = True; r.font.color.rgb = ACC


def bullets_slide(prs, title, bullets, footer="AI-901 FDP"):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(s); _accent_bar(s); _title(s, title)
    _, tf = _box(s, Inches(0.8), Inches(1.5), Inches(11.8), Inches(5.4))
    first = True
    for b in bullets:
        indent = 0
        text = b
        if isinstance(b, tuple):
            indent, text = b
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.level = indent
        p.space_after = Pt(8)
        # marker
        mk = p.add_run()
        mk.text = ("•  " if indent == 0 else "–  ")
        mk.font.color.rgb = ACC2 if indent == 0 else WARN
        mk.font.size = Pt(20 if indent == 0 else 17)
        mk.font.bold = True
        # text (supports **bold** segments)
        for seg, is_bold in _parse_bold(text):
            r = p.add_run(); r.text = seg
            r.font.size = Pt(20 if indent == 0 else 17)
            r.font.color.rgb = WHITE if is_bold else INK
            r.font.bold = is_bold
    _footer(s, footer)
    return s


def two_col_slide(prs, title, left_head, left_items, right_head, right_items, footer="AI-901 FDP"):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(s); _accent_bar(s); _title(s, title)
    for x, head, items in [(Inches(0.8), left_head, left_items),
                           (Inches(7.0), right_head, right_items)]:
        card = s.shapes.add_shape(5, x, Inches(1.6), Inches(5.6), Inches(5.2))
        card.fill.solid(); card.fill.fore_color.rgb = CARD
        card.line.color.rgb = ACC; card.line.width = Pt(1)
        tf = card.text_frame; tf.word_wrap = True
        tf.margin_left = Inches(0.3); tf.margin_right = Inches(0.3); tf.margin_top = Inches(0.25)
        p = tf.paragraphs[0]; r = p.add_run(); r.text = head
        r.font.size = Pt(22); r.font.bold = True; r.font.color.rgb = ACC2
        p.space_after = Pt(10)
        for it in items:
            pp = tf.add_paragraph(); pp.space_after = Pt(6)
            mk = pp.add_run(); mk.text = "•  "; mk.font.color.rgb = ACC; mk.font.bold = True; mk.font.size = Pt(16)
            for seg, is_bold in _parse_bold(it):
                r = pp.add_run(); r.text = seg; r.font.size = Pt(16)
                r.font.color.rgb = WHITE if is_bold else INK; r.font.bold = is_bold
    _footer(s, footer)
    return s


def trap_slide(prs, title, trap_text, footer="AI-901 FDP"):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    _bg(s); _accent_bar(s); _title(s, title)
    card = s.shapes.add_shape(5, Inches(0.8), Inches(2.4), Inches(11.7), Inches(2.3))
    card.fill.solid(); card.fill.fore_color.rgb = RGBColor(0x23, 0x1A, 0x08)
    card.line.color.rgb = WARN; card.line.width = Pt(2)
    tf = card.text_frame; tf.word_wrap = True
    tf.margin_left = Inches(0.4); tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    mk = p.add_run(); mk.text = "⚠  EXAM TRAP  —  "; mk.font.bold = True; mk.font.size = Pt(22); mk.font.color.rgb = WARN
    for seg, is_bold in _parse_bold(trap_text):
        r = p.add_run(); r.text = seg; r.font.size = Pt(22)
        r.font.color.rgb = WHITE if is_bold else INK; r.font.bold = is_bold
    _footer(s, footer)
    return s


def _footer(slide, text):
    _, tf = _box(slide, Inches(0.7), Inches(7.02), Inches(9), Inches(0.4))
    p = tf.paragraphs[0]; r = p.add_run(); r.text = text
    r.font.size = Pt(11); r.font.color.rgb = MUTE


def _parse_bold(text):
    """Split '**bold**' markers into (segment, is_bold) pairs."""
    out, buf, i, bold = [], "", 0, False
    while i < len(text):
        if text[i:i+2] == "**":
            if buf:
                out.append((buf, bold)); buf = ""
            bold = not bold; i += 2
        else:
            buf += text[i]; i += 1
    if buf:
        out.append((buf, bold))
    return out or [(text, False)]


# ============================ CONTENT ============================

def build_day3():
    prs = new_deck()
    title_slide(prs, "DAY 3 · 07-Jul", "Foundations, Responsible AI,\nFoundry & Computer Vision",
                "Microsoft Certified: Azure AI Fundamentals — Exam AI-901")
    two_col_slide(prs, "AI-901 is NOT AI-900",
        "Old (AI-900, retired)", ["Services in **isolation**", "**No coding**", "Form Recognizer, LUIS, QnA Maker"],
        "New (AI-901)", ["Build in **Microsoft Foundry**", "Assumes **basic Python + SDK**", "Agents + **Content Understanding**"])
    bullets_slide(prs, "Exam facts", [
        "Code **AI-901** · pass **700 / 1000** (scaled)",
        "~40–60 questions · ~45–60 minutes · ~$99 USD · never expires",
        "Domain 1 — Identify AI concepts & capabilities  **(40–45%)**",
        "Domain 2 — Implement with Microsoft Foundry  **(55–60%)**",
        "Teach **lab-first**: more than half the exam is *doing* it in Foundry"])
    bullets_slide(prs, "AI workloads — scenario → capability", [
        "**Create** text/images/video/code → generative models",
        "**Act** with tools + multi-step → agent",
        "**Understand text** → sentiment · entities · keywords · summary",
        "**Speech** → STT (recognition) / TTS (synthesis)",
        "**Vision** → classify · detect · OCR · describe",
        "**Extract** structured fields → Content Understanding"])
    bullets_slide(prs, "Responsible AI — F.R.I.T.A.P.", [
        "**Fairness** — no bias across groups",
        "**Reliability & Safety** — the *system* behaves safely",
        "**Inclusiveness** — everyone, all abilities",
        "**Transparency** — disclose it's AI + its limits",
        "**Accountability** — *people/orgs* answerable + governance",
        "**Privacy & Security** — protect data + secure the system"])
    trap_slide(prs, "The trap examiners love",
        "Reliability & Safety = the **system** behaves correctly. Accountability = **people** are answerable. Oversight board → **Accountability**.")
    bullets_slide(prs, "How generative AI models work", [
        "**Token** — unit of text; limits & billing are token-based",
        "**Embedding** — numeric vector of meaning → search / RAG",
        "**Transformer** — architecture using *attention*",
        "LLMs **predict the next token** (not a DB lookup) → can hallucinate",
        "Fix hallucination with **grounding / RAG**",
        "**Multimodal** = also handles images / audio"])
    bullets_slide(prs, "Microsoft Foundry — where you build", [
        "Portal at **ai.azure.com** (no-code) · **SDK** for code",
        "**Hub** (top workspace) → **Project** (a solution) → **Deployment** (callable model)",
        "Deploy from the **model catalog**; note the **deployment name**",
        "Reach it via an **endpoint** + auth (key or Microsoft Entra ID)",
        "**Tools**: Azure Speech, Content Understanding, grounding/search"])
    trap_slide(prs, "Config trap",
        "**temperature / top_p = randomness**. **max_tokens = length**. Never mix them up.")
    bullets_slide(prs, "Computer vision — capabilities", [
        "**Image classification** — one whole-image label",
        "**Object detection** — labels + **bounding boxes** (where)",
        "**OCR** — read text inside an image",
        "**Image description** — caption / tags",
        "How it works: pixels → **CNN** → **Vision Transformer / multimodal**"])
    bullets_slide(prs, "Generate images & video", [
        "**Image-generation** (DALL·E 3 / GPT-image) → still images from text",
        "**Video-generation** → short clips from text  *(new in AI-901)*",
        "**Multimodal** → *understands* images/video as input",
        "Interpret an image: attach it inside the **user** message content",
        "All governed by **Content Safety**"])
    bullets_slide(prs, "Day 3 lab & homework", [
        "**Lab 1** — deploy GPT-4o-mini, chat, move temperature/max_tokens",
        "Vision playground: describe a photo + read its text",
        "Deploy an image model; generate 2 images",
        "Then: **Practice Test 1, Q1–20**"])
    prs.save(os.path.join(HERE, "AI-901_Day3_Foundations-Vision.pptx"))


def build_day4():
    prs = new_deck()
    title_slide(prs, "DAY 4 · 08-Jul", "Text Analysis, Speech &\nInformation Extraction",
                "NLP concepts · Azure Speech in Foundry Tools · Azure Content Understanding")
    bullets_slide(prs, "How NLP works — 3 layers", [
        "**Tokenization** — split text into tokens",
        "**Statistical** — word counts / TF-IDF / bag-of-words (no real meaning)",
        "**Semantic** — embeddings + transformers = meaning & context",
        "Cue: 'word frequency' → statistical · 'synonyms match' → semantic"])
    bullets_slide(prs, "Four text-analysis techniques", [
        "**Keyword extraction** — main talking points",
        "**Entity detection (NER)** — Person / Location / Org / Date",
        "**Sentiment analysis** — positive / negative / neutral / **mixed**",
        "**Summarization** — a shorter version",
        "Also: language detection · PII · entity linking · CLU · question answering"])
    trap_slide(prs, "NLP trap",
        "CLU = **intent / action** ('cancel my booking'). Question answering = **FAQ from a knowledge base**. LUIS→CLU, QnA Maker→question answering.")
    bullets_slide(prs, "Implement text analysis in Foundry", [
        "Prompt a model with a **system** message: 'return JSON: sentiment, key_phrases, entities, summary'",
        "Use **temperature = 0** for deterministic analysis",
        "**Model + prompt** = flexible, multilingual, less deterministic",
        "**Azure Language tool** = consistent, structured, prebuilt"])
    two_col_slide(prs, "Speech — two capabilities",
        "Speech recognition", ["**audio → text** (STT)", "transcription, captions, commands"],
        "Speech synthesis", ["**text → audio** (TTS)", "neural voices, SSML"])
    bullets_slide(prs, "Speech in AI-901 implementation", [
        "**Azure Speech in Foundry Tools** — STT/TTS apps",
        "**Speech-capable agent** — users talk to it",
        "**Multimodal audio model** — hear + reply with one model",
        "Cue: 'transcribe' → STT · 'read aloud' → TTS · 'translate spoken' → speech translation"])
    bullets_slide(prs, "Information extraction basics", [
        "**OCR** — detect & read text inside images/scans (first step)",
        "**Field extraction & mapping** — value → named field (number → total)",
        "That mapping is exactly a Content Understanding **field schema**"])
    bullets_slide(prs, "Azure Content Understanding", [
        "One multimodal service: **documents, images, audio, video**",
        "Define an **analyzer** + **field schema** (the fields to extract)",
        "Returns **structured JSON** (field = value + confidence)",
        "Build a lightweight extraction app on top"])
    trap_slide(prs, "Extraction trap",
        "50,000 invoices → structured fields = **Content Understanding**. One ad-hoc question about a single photo = **prompt a multimodal model**.")
    bullets_slide(prs, "Day 4 labs & homework", [
        "**Text lab** — model returns sentiment + entities + summary as JSON",
        "**Speech lab** — STT a clip, TTS a sentence, tweak a voice",
        "**Lab 4** — Content Understanding invoice analyzer → read JSON",
        "Then: **Practice Test 1, Q21–40**"])
    prs.save(os.path.join(HERE, "AI-901_Day4_Text-Speech-Extraction.pptx"))


def build_day5():
    prs = new_deck()
    title_slide(prs, "DAY 5 · 09-Jul", "Generative AI, Agents &\nthe Foundry SDK",
                "The heart of AI-901 — Domain 2 (55–60% of the exam)")
    bullets_slide(prs, "Prompts — the three roles", [
        "**system** — persona · rules · grounding · format · guardrails",
        "**user** — the actual request (+ image/audio)",
        "**assistant** — prior replies (context)",
        "Techniques: clear instructions · few-shot · grounding · chain-of-thought",
        "Chat models are **stateless per call** — the app resends history"])
    trap_slide(prs, "Prompt trap",
        "Rules and grounding go in the **system** message — never the user message.")
    bullets_slide(prs, "Lightweight chat client (Foundry SDK)", [
        "3 things to call a model: **endpoint · credential · deployment name**",
        "client.chat.completions.create(model=deployment, messages=[...])",
        "Read the reply at **response.choices[0].message.content**",
        "Auth: API **key** or **Microsoft Entra ID** (DefaultAzureCredential)"])
    bullets_slide(prs, "Pick the right model", [
        "**Reasoning (o-series)** — complex multi-step logic/math",
        "**Small (4o-mini / Phi)** — cheap, fast, high-volume simple",
        "**Multimodal** — image/audio input",
        "**Image-gen / Video-gen** — create visuals",
        "**Embeddings** — search / similarity / RAG",
        "Choose by capability · cost · latency · context window"])
    two_col_slide(prs, "Deployment types & config",
        "Deployment types", ["Standard / Global Standard (pay-go)", "**PTU** — reserved, predictable latency",
                              "Batch — async bulk", "Serverless / Managed compute"],
        "Inference params", ["**temperature/top_p** = randomness", "**max_tokens** = length",
                             "**freq/presence penalty** = repetition", "**seed** = repeatable · **stop** = halt"])
    trap_slide(prs, "Deployment trap",
        "Steady high-volume with predictable latency → **Provisioned Throughput (PTU)**. Batch = async bulk. Standard = pay-go, no reservation.")
    bullets_slide(prs, "Agents — the equation", [
        "**Agent = model + instructions + tools (+ knowledge)** that can *act*",
        "Tools: code interpreter · file search / knowledge · function calling · search",
        "Agent vs chat: agent **uses tools & acts**; chat = text-in/text-out",
        "Lifecycle: **create agent → thread → message → run → read messages**"])
    bullets_slide(prs, "Build & run a single agent", [
        "Portal: pick model → write **instructions** → add **tools/knowledge** → test",
        "SDK: create_agent(model, instructions) ",
        "  create_thread() → create_message(user) → create_and_process_run()",
        "  list_messages() to read the reply",
        "A **run** is what executes reasoning + tool calls"])
    bullets_slide(prs, "Grounding & safety", [
        "**Grounding / RAG** — retrieve your data → add to prompt → fewer hallucinations",
        "**Content Safety** — content filters (hate/violence/…)",
        "**Prompt shields** — defend against prompt injection / jailbreak",
        "**Evaluations** — groundedness · relevance · safety"])
    bullets_slide(prs, "Day 5 labs", [
        "**Lab 2** — SDK chat client; change system message + temperature",
        "**Lab 3** — single agent with file-search over a PDF, then run from SDK",
        "Then: **Practice Test 2** (live workshop)"])
    prs.save(os.path.join(HERE, "AI-901_Day5_GenAI-Agents-SDK.pptx"))


def build_day6():
    prs = new_deck()
    title_slide(prs, "DAY 6 · 10-Jul", "Rapid Revision, Exam Traps\n& Mock Certification Test",
                "Memory sheets · decision tree · 50-question mock")
    bullets_slide(prs, "Top exam traps", [
        "**temperature/top_p = randomness · max_tokens = length**",
        "Reliability & Safety (system) ≠ Accountability (people)",
        "Code references the **deployment name**, not the base model",
        "Rules/grounding → **system** message",
        "Multimodal *understands* · image/video-gen *create*",
        "Agent uses tools & acts; chat = text-in/text-out",
        "Structured extraction from files → **Content Understanding + field schema**",
        "Grounding/RAG fixes hallucination (not higher temperature)"])
    two_col_slide(prs, "Memory sheets",
        "Concepts", ["F.R.I.T.A.P. (6 principles)", "token · embedding · transformer",
                     "temp/top_p=random · max_tokens=length", "Deploy: Standard/GlobalStd/PTU/Batch/Serverless"],
        "Foundry", ["Hub → Project → Deployment", "messages→choices[0].message.content",
                    "agent→thread→message→run→read", "Content Understanding: analyzer + field schema"])
    bullets_slide(prs, "Decision tree (say it out loud)", [
        "Create content? → text=generative · image=image-gen · video=video-gen",
        "Act with tools / multi-step? → **agent**",
        "Understand image/audio? → **multimodal**",
        "audio→text = STT · text→audio = TTS",
        "Analyze text? → text analysis · Fields from files? → **Content Understanding**"])
    bullets_slide(prs, "Mock Certification Test", [
        "**50 questions · 60 minutes · closed book** · pass ≈ 35/50",
        "Read 'choose TWO/THREE' carefully",
        "Name the capability first, then the Foundry way to build it",
        "Flag & return to hard items — don't stall",
        "Sandbox the exam UI first: aka.ms/examdemo",
        "Review **every** answer together afterwards"])
    title_slide(prs, "", "You're ready.", "Register with a personal Microsoft account · pass = 700/1000 · cert never expires.")
    prs.save(os.path.join(HERE, "AI-901_Day6_Revision-Mock.pptx"))


if __name__ == "__main__":
    build_day3(); build_day4(); build_day5(); build_day6()
    print("Built decks in:", HERE)
    for f in sorted(os.listdir(HERE)):
        if f.endswith(".pptx"):
            print("  -", f)

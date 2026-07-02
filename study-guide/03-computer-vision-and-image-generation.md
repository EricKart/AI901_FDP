# Module 03 — Computer Vision & Image Generation
### Day 3 · Session 2 | Domain 1 (identify CV & image-gen capabilities) + Domain 2 (implement vision in Foundry)

AI-901 splits vision into two things: **understanding** images (now done with **multimodal models**) and **generating** images (**image-generation models**). The old "pick Azure AI Vision vs Custom Vision" framing is de-emphasized — you now mostly **prompt a multimodal model** in Foundry.

---

## PART A — Computer vision concepts (Domain 1)

Computer vision = software that **interprets images and video**. Recognize these capabilities and map scenarios to them:

| Capability | Question it answers | Output | Needs location? |
|---|---|---|---|
| **Image classification** | "What *is* this image?" | Whole-image **label(s)** | No |
| **Object detection** | "*What* objects and *where*?" | Labels **+ bounding boxes** | **Yes** |
| **OCR (read text)** | "What *text* is in this image?" | Extracted text + location | Text region |
| **Image description / captioning** | "Describe this image" | Natural-language caption, tags | Mixed |
| **Face detection** | "Are there faces / where?" | Face rectangles, landmarks | Yes |
| **Image generation** | "Create an image of…" | A **new image** from a text prompt | — |

> ⭐ **Classic trap — classification vs detection:** just a whole-image label → **classification**; label **+ a box saying where** (and can find multiple objects) → **object detection**. *"Count and mark each car in a photo"* → object detection.

### Multimodal models do vision understanding now
In AI-901, to "understand" an image you typically **send the image to a multimodal model** (e.g., GPT-4o) with a prompt like *"Describe this image"* or *"What is the licence-plate number?"*. The model can caption, read text, answer questions about the image, classify, etc. — all via prompting. This is the **"interpret visual input in prompts by using a deployed multimodal model"** exam objective.

### How vision models work (recognize these terms — from the official concepts module)
- **Image processing** basics: an image is a grid of **pixels**; filters/convolutions detect edges, textures, shapes.
- **Convolutional Neural Networks (CNNs)** — the classic deep-learning architecture for image classification/detection; learn hierarchical visual features.
- **Vision Transformers (ViT) & multimodal models** — newer architecture that applies transformer **attention** to image patches; underpins **multimodal** models (e.g., GPT-4o) that reason over images **and** text together.
> You won't do the math on the exam, but you must recognize *CNN*, *vision transformer*, and *multimodal* and what each is for.

### Image-generation models
- **DALL·E 3** and **GPT-image** generate images from **text prompts** (and can edit/vary images).
- Use cases: concept art, mock-ups, marketing visuals, variations.
- Governed by **Responsible AI / Content Safety** (blocks disallowed content; provenance/watermarking).

### Video-generation models ⭐ (new in AI-901 — don't miss this)
- Foundry's computer-vision coverage now includes **video-generation models** that produce **short video clips** from text (and/or image) prompts.
- Recognize the trio of *generative* visual model types: **image-generation** (still images), **video-generation** (clips), and **multimodal** (understand images/video as input).

> **Exam trap:** *analyze/describe an existing image* → **multimodal (vision) model**. *create a still image* → **image-generation model**. *create a video clip* → **video-generation model**. Different jobs, different model types.

---

## PART B — Implementing vision in Foundry (Domain 2)

Three exam objectives here: **interpret visual input** with a multimodal model, **create visual outputs** with a generative model, and **build a lightweight vision app**.

### 1) Interpret an image with a multimodal model (chat with an image)
In the Foundry **playground** (or via SDK), attach an image and ask about it. In code, an image is passed as part of the user message content:

```python
# Vision understanding with a multimodal chat model (illustrative)
from openai import AzureOpenAI
client = AzureOpenAI(azure_endpoint=ENDPOINT, api_key=KEY, api_version="2024-10-21")

response = client.chat.completions.create(
    model="gpt-4o",  # your multimodal deployment name
    messages=[
        {"role": "system", "content": "You describe images for accessibility."},
        {"role": "user", "content": [
            {"type": "text", "text": "Describe this image and read any text in it."},
            {"type": "image_url", "image_url": {"url": "https://example.com/photo.jpg"}}
        ]}
    ],
)
print(response.choices[0].message.content)
```
Key idea for the exam: the **user message can contain both text and an image**; a **multimodal deployment** is required.

### 2) Generate an image from text
In the Foundry playground pick an **image model** and prompt it; in code:

```python
# Image generation (illustrative)
result = client.images.generate(
    model="dall-e-3",            # your image-model deployment name
    prompt="A watercolor fox in a snowy forest, soft light",
    size="1024x1024", n=1,
)
print(result.data[0].url)        # link to the generated image
```

### 3) Lightweight vision app
Combine the above: take a user's uploaded image → send to multimodal model → return a caption/answer; or take a text prompt → return a generated image. That's the "lightweight application that includes vision capabilities" objective.

---

## C. Session 2 live-demo checklist
1. **Foundry playground**: upload a photo to a **GPT-4o** deployment; ask "Describe this" and "Read the text in this image." (Shows captioning + OCR without a separate OCR service.)
2. Ask the same model to **count objects** — contrast "describe" vs "locate/count."
3. **Deploy an image model** (DALL·E 3 / GPT-image) and generate 2 images from prompts; tweak the prompt to show prompt sensitivity.
4. Point out the **content filter** blocking a disallowed image request → Responsible AI tie-in.

## D. Scenario drill
| Scenario | Answer |
|---|---|
| Describe a photo aloud for a blind user | **Multimodal model (vision)** + speech synthesis |
| Read printed/handwritten text from a photo | Multimodal model (OCR) *or* image-analysis read |
| Create a marketing image from a description | **Image-generation model (DALL·E/GPT-image)** |
| Find and box every product on a shelf | **Object detection** |
| One label: is this a cat or a dog? | **Image classification** |
| Answer "how many people are in this image?" | **Multimodal model** (vision reasoning) |

## E. Rapid recall
1. Bounding boxes + multiple objects = ? *(object detection)*
2. Understand/answer questions about an existing image → which model type? *(multimodal)*
3. Create a new image from text → ? *(image-generation model)*
4. In a chat request, an image is attached inside which message? *(the **user** message content)*
5. What Responsible-AI control gates disallowed image generation? *(Content Safety / content filter)*

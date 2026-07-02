# generative-ai-experiments-fastapi

FastAPI experiments for serving generative AI models locally. Chapter 3 includes text-to-audio (Bark) and text-to-image (Stable Diffusion) APIs.

## Prerequisites

- Python 3.10+
- A machine with enough RAM/VRAM to run the chosen model (CPU works but is slow)
- [Hugging Face](https://huggingface.co/) account optional; models download on first run

## Installation

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

For the optional Streamlit audio client:

```bash
pip install streamlit requests
```

## Project structure

```
ch-3/
├── audio-models/     # Text-to-speech with suno/bark-small
│   ├── main.py       # FastAPI app
│   ├── models.py     # Model loading and generation
│   ├── schemas.py    # Voice preset types
│   ├── utils.py      # Audio buffer helpers
│   └── client.py     # Streamlit chat UI
└── vision-models/    # Text-to-image with segmind/tiny-sd
    ├── main.py       # FastAPI app
    ├── models.py     # Pipeline loading and generation
    └── utils.py      # Image encoding helpers
```

## Audio API (text-to-speech)

From `ch-3/audio-models/`:

```bash
uvicorn main:app --reload
```

| Endpoint | Method | Parameters | Response |
|----------|--------|------------|----------|
| `/generate/audio` | GET | `prompt` (required), `preset` (optional, default `v2/en_speaker_1`) | Audio stream |

**Voice presets:** `v2/en_speaker_1`, `v2/en_speaker_9`

**Example:**

```bash
curl "http://localhost:8000/generate/audio?prompt=Hello%20world" --output speech.wav
```

**Streamlit client** (with the API running on port 8000):

```bash
cd ch-3/audio-models
streamlit run client.py
```

## Vision API (text-to-image)

From `ch-3/vision-models/`:

```bash
uvicorn main:app --reload
```

| Endpoint | Method | Parameters | Response |
|----------|--------|------------|----------|
| `/generate/image` | GET | `prompt` (required) | PNG image |

**Example:**

```bash
curl "http://localhost:8000/generate/image?prompt=a%20cat%20on%20a%20mat" --output image.png
```

## Models

| Service | Model | Library |
|---------|-------|---------|
| Audio | [suno/bark-small](https://huggingface.co/suno/bark-small) | `transformers` |
| Vision | [segmind/tiny-sd](https://huggingface.co/segmind/tiny-sd) | `diffusers` |

Models are downloaded from Hugging Face on first request and cached locally.

## Interactive docs

With either app running, open:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Notes

- Run only one service per port, or start each on a different port (e.g. `--port 8001`).
- First inference after startup can take several minutes while weights load.
- These endpoints are intended for local experimentation, not production use.

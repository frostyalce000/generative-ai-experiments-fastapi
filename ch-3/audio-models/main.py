from fastapi import FastAPI, Query, status
from typing import Annotated
from fastapi.responses import StreamingResponse
from models import load_audio_model, generate_audio
from schemas import VoicePresets
from utils import audio_array_to_buffer


app = FastAPI()


@app.get("/generate/audio")
def serve_text_to_audio_model_controller(
        prompt = Annotated[Query(...), "User Prompt"],
        preset: VoicePresets = Query(default="v2/en_speaker_1")
):
    processor, model = load_audio_model()
    output, sample_rate = generate_audio(processor, model, prompt, preset)
    return StreamingResponse(audio_array_to_buffer(output, sample_rate))
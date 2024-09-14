import torch
from diffusers import DiffusionPipeline, StableDiffusionInpaintPipelineLegacy
from PIL import Image


def load_image_model() -> StableDiffusionInpaintPipelineLegacy:
    pipe = DiffusionPipeline.from_pretrained(
        "segmind/tiny-sd", torch_dtype=torch.float32
    )
    return pipe


def generate_image(
        pipe: StableDiffusionInpaintPipelineLegacy, prompt: str
) -> Image.Image:
    output = pipe(prompt, num_inference_stepts=10).images[0]
    return output

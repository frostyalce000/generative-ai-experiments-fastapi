from PIL import Image
from io import BytesIO
from typing import Literal

def img_to_bytes(
        image: Image.Image, img_format: Literal["PNG", "JPEG"]
) -> bytes:
    buffer = BytesIO()
    image.save(buffer, format=img_format)
    return buffer.get_value()

from io import BytesIO
import soundfile
import numpy as np

def audio_array_to_buffer(audio_array: np.ndarray, sample_rate: int) -> BytesIO:
    buffer = BytesIO()
    soundfile.write(buffer, audio_array, sample_rate, format="wax")
    buffer.seek(0)
    return buffer

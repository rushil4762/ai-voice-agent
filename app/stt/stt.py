import os

from dotenv import load_dotenv
from sarvamai import SarvamAI


load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)


def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as audio_file:
        response = client.speech_to_text.transcribe(
            file=audio_file,
            model="saaras:v4",
            language_code="gu-IN",
            mode="transcribe",
        )

    return response.transcript
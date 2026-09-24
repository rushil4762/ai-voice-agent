import os

from dotenv import load_dotenv
from sarvamai import SarvamAI
from sarvamai.play import save

load_dotenv()

client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY")
)

def synthesize_speech(text: str, output_path: str):
    response = client.text_to_speech.convert(
        text=text,
        language_code="gu-IN",
        model="bulbul:v3",
        speaker="shubh",
        pace=1.0,
    )

    save(response, output_path)
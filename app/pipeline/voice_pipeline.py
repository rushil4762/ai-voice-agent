from app.stt.stt import transcribe_audio
from app.llm.llm import generate_response
from app.tts.tts import synthesize_speech
from app.utils.audio import play_audio


def run_voice_pipeline(audio_path: str, output_path: str):
    print("\n[1/4] Converting speech to text...")

    user_text = transcribe_audio(audio_path)
    print(f"User: {user_text}")

    print("\n[2/4] Generating AI response...")

    response_text = generate_response(user_text)
    print(f"AI: {response_text}")

    print("\n[3/4] Converting AI response to speech...")

    synthesize_speech(response_text, output_path)
    print(f"Audio generated: {output_path}")

    print("\n[4/4] Playing AI response...")

    play_audio(output_path)
    print("Audio playback completed.")

    return {
        "user_text": user_text,
        "response_text": response_text,
        "audio_path": output_path,
    }
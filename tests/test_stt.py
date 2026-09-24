from app.stt.stt import transcribe_audio


audio_path = "data/audio/user.m4a"

text = transcribe_audio(audio_path)

print("\n--- STT RESULT ---")
print(text)
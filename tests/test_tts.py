from app.tts.tts import synthesize_speech

text = "નમસ્તે! આજે તમે કેમ છો? હું તમારી મદદ કરવા માટે અહીં છું."

output_path = "data/audio/tts_output.wav"

synthesize_speech(text, output_path)

print("\n--- TTS RESULT ---")
print(f"Audio generated successfully: {output_path}")
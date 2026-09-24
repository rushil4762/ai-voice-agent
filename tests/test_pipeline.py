from app.pipeline.voice_pipeline import run_voice_pipeline


audio_path = "data/audio/user.m4a"
output_path = "data/audio/pipeline_output.wav"

result = run_voice_pipeline(
    audio_path=audio_path,
    output_path=output_path,
)

print("\n--- PIPELINE RESULT ---")
print(f"User text: {result['user_text']}")
print(f"AI response: {result['response_text']}")
print(f"Audio: {result['audio_path']}")
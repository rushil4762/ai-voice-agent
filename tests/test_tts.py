from app.tts.tts import synthesize_speech

text = "હા, જરૂર. હું તમારી એપોઇન્ટમેન્ટ બુક કરવામાં તમારી મદદ કરીશ. કૃપા કરીને જણાવો કે તમે કયા દિવસે અને કેટલા વાગ્યે એપોઇન્ટમેન્ટ લેવા માંગો છો?"

output_path = "data/audio/appointment_response.wav"

synthesize_speech(text, output_path)

print("\n--- TTS RESULT ---")
print(f"Audio generated successfully: {output_path}")
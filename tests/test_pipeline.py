from app.pipeline.voice_pipeline import run_voice_pipeline


conversation_history = []

audio_path = "data/audio/user.wav"
output_path = "data/audio/pipeline_output.wav"


print("\n======================================")
print(" Hospital Voice Assistant")
print("======================================")

while True:

    print("\nSpeak your next message and save it as:")
    print("data/audio/user.wav")

    input("\nPress ENTER when the new recording is ready...")

    result = run_voice_pipeline(
        audio_path=audio_path,
        output_path=output_path,
        conversation_history=conversation_history,
    )

    print("\n--------------------------------------")
    print("Conversation History")
    print("--------------------------------------")

    for message in conversation_history:
        print(f"{message['role']}: {message['text']}")

    print("--------------------------------------")

    choice = input("\nContinue conversation? (y/n): ").strip().lower()

    if choice != "y":
        print("\nConversation ended.")
        break
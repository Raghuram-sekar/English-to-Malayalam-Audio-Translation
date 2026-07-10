import whisper

# Load the Whisper model
model = whisper.load_model("base")  # You can use "small" or "medium" for better accuracy

# Transcribe the audio file
result = model.transcribe("audioclip.wav")
print("Transcription:", result["text"])

# Save the transcription to a file
with open("english_transcription.txt", "w", encoding="utf-8") as f:
    f.write(result["text"]) 
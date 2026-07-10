from pydub import AudioSegment

# List your audio parts in order
audio_files = ["malayalam_translated-part1.mp3", "malayalam_translated-part2.mp3"]  # Add more if needed

# Start with the first file
combined = AudioSegment.from_mp3(audio_files[0])

# Append the rest
for file in audio_files[1:]:
    combined += AudioSegment.from_mp3(file)

# Export the combined audio as WAV
combined.export("malayalam_speech_full.wav", format="wav")
print("Combined audio saved as malayalam_speech_full.wav") 
from pydub import AudioSegment
import os

# Path to your MP3 file
mp3_path = "audioclip.mp3"  # File in project root
wav_path = "audioclip.wav"

# Convert MP3 to WAV
audio = AudioSegment.from_mp3(mp3_path)
audio.export(wav_path, format="wav")
print(f"Converted {mp3_path} to {wav_path}") 
from TTS.api import TTS

# Load YourTTS model (supports voice cloning and Malayalam)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True, gpu=False)

# Read the Malayalam translation
with open("malayalam_translation.txt", "r", encoding="utf-8") as f:
    malayalam_text = f.read()

# Synthesize speech using your voice sample
tts.tts_to_file(
    text=malayalam_text,
    speaker_wav="myvoice.wav",  # User's voice sample
    language="ml",
    file_path="malayalam_speech.wav"
) 
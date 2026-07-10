import torch
# Allowlist the XttsConfig class for torch.load (PyTorch 2.6+ workaround)
torch.serialization.add_safe_globals(['TTS.tts.configs.xtts_config.XttsConfig'])

from TTS.api import TTS

# Load XTTS v2 model (multilingual, default voice)
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True, gpu=False)

# Read the Malayalam translation
with open("malayalam_translation.txt", "r", encoding="utf-8") as f:
    malayalam_text = f.read()

# Synthesize speech (no speaker_wav for default voice)
tts.tts_to_file(
    text=malayalam_text,
    speaker="random",
    language="ml",
    file_path="malayalam_speech.wav"
) 
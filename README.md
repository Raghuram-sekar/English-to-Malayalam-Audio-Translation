# English-to-Malayalam Audio Translation and Synthesis Project
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white) ![License](https://img.shields.io/badge/License-MIT-green.svg)

## Overview
This project demonstrates a full pipeline for translating an English audio dialogue into Malayalam and generating Malayalam speech audio. The process includes speech-to-text, translation, and text-to-speech (TTS) synthesis, with all steps automated or semi-automated using open-source tools and free online services.

---

## Steps and Tools Used

### 1. **Audio Preparation**
- **Input:** English audio file (MP3)
- **Conversion:** Used a Python script with `pydub` to convert MP3 to WAV for compatibility with speech-to-text models.

### 2. **Speech-to-Text (Transcription)**
- **Tool:** OpenAI Whisper (via Hugging Face)
- **Script:** `transcribe_audio.py`
- **Output:** English transcription saved as `english_transcription.txt`

### 3. **Translation (English to Malayalam)**
- **Tool:** Hugging Face Transformers (`Helsinki-NLP/opus-mt-en-ml`)
- **Script:** `translate_to_malayalam.py`
- **Improvement:** Translation was updated to process text sentence-by-sentence for better accuracy.
- **Output:** Malayalam translation saved as `malayalam_translation.txt`

### 4. **Text-to-Speech (Malayalam Audio Synthesis)**
- **Challenge:** No open-source TTS model with voice cloning supports Malayalam.
- **Solution:** Used free online TTS services (e.g. FreeTTS) to generate Malayalam audio in parts due to character limits.
- **Output:** Multiple Malayalam audio files (e.g., `malayalam_translated-part1.mp3`, `malayalam_translated-part2.mp3`)

### 5. **Audio Joining**
- **Tool:** Python script with `pydub` (`join_audio.py`)
- **Process:** Combined multiple MP3 files into a single WAV file (`malayalam_speech_full.wav`).

---

## Scripts
- `convert_mp3_to_wav.py` — Converts MP3 to WAV
- `transcribe_audio.py` — Transcribes WAV audio to English text
- `translate_to_malayalam.py` — Translates English text to Malayalam (sentence-by-sentence)
- `join_audio.py` — Joins multiple audio files into one

---

## Challenges & Solutions

- **Python Version Compatibility:**
  - `pydub` and many audio libraries do not work with Python 3.13+ due to removal of `audioop`.
  - **Solution:** Used Python 3.12 or 3.11 for all audio processing steps.

- **TTS Model Language Support:**
  - Coqui TTS and XTTS v2 do not support Malayalam (`ml`), only major languages like English, Hindi, etc.
  - **Solution:** Used free online TTS services for Malayalam audio.

- **Large Text/Audio Limits:**
  - Online TTS services have character limits per request.
  - **Solution:** Split Malayalam text into parts, generated audio for each, and joined them using `pydub`.

- **Voice Cloning for Malayalam:**
  - No open-source model supports Malayalam voice cloning as of now.
  - **Solution:** Used default/robotic voices for Malayalam TTS.

- **Model Download/Installation Issues:**
  - Large models (Whisper, XTTS) require stable internet and compatible PyTorch/torchaudio versions.
  - **Solution:** Downgraded PyTorch and torchaudio as needed, retried downloads, and followed error messages for fixes.

---

## How to Reproduce
1. Place your English audio file in the project folder.
2. Run `convert_mp3_to_wav.py` to convert to WAV.
3. Run `transcribe_audio.py` to get English text.
4. Run `translate_to_malayalam.py` to get Malayalam text.
5. Use an online Malayalam TTS (e.g., Bhashini) to generate audio for each part of the Malayalam text.
6. Download the audio files and rename as `part1.mp3`, `part2.mp3`, etc.
7. Run `join_audio.py` to combine them into `malayalam_speech_full.wav`.

---

## Notes
- All scripts are designed to be run from the project root.
- For best results, use Python 3.12 or 3.11 for all scripts.
- Free online TTS services may change their terms or availability over time.

---

## Credits
- OpenAI Whisper
- Hugging Face Transformers
- Bhashini (Government of India TTS)
- pydub (audio processing)

---
# Made by Raghuram Sekar

---
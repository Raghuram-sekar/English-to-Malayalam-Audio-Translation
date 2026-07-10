from transformers import pipeline
import re

# Load the translation pipeline
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ml")

# Read the English transcription
with open("english_transcription.txt", "r", encoding="utf-8") as f:
    english_text = f.read()

# Split into sentences (simple split, can be improved)
sentences = re.split(r'(?<=[.!?]) +', english_text)

# Translate each sentence and join
malayalam_sentences = []
for sentence in sentences:
    if sentence.strip():
        translated = translator(sentence.strip())
        malayalam_sentences.append(translated[0]['translation_text'])

malayalam_text = '\n'.join(malayalam_sentences)
print("Malayalam Translation:", malayalam_text)

# Save the Malayalam translation
with open("malayalam_translation.txt", "w", encoding="utf-8") as f:
    f.write(malayalam_text) 
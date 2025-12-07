import os
os.environ['WHISPER_CACHE'] = r'C:\whisper-poc\models\whisper'

import whisper

print("Lade Medium Modell...")
model = whisper.load_model('medium')

print("\n✓ Modell geladen!")
print(f"Modell: {model}")
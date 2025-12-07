import os
os.environ['WHISPER_CACHE'] = r'C:\whisper-poc\models\whisper'

import whisper
import sounddevice as sd
import soundfile as sf
import numpy as np

print("Lade Modell...")
model = whisper.load_model('medium')

print("\n" + "="*60)
print("LIVE MICROPHONE TEST")
print("="*60)
print("Spreche jetzt 10 Sekunden lang...")
print("(Die Audio wird aufgenommen)")

# Aufnahme starten
duration = 10
sample_rate = 16000
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
sd.wait()

# Speichere temporär
temp_file = 'temp_audio.wav'
sf.write(temp_file, audio, sample_rate)

# Transkribiere
print("\nTranskribiere...")
result = model.transcribe(temp_file, language='de')

print("\n" + "="*60)
print("ERKANNTER TEXT:")
print("="*60)
print(result['text'])

# Aufräumen
import os
os.remove(temp_file)
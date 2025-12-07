import sounddevice as sd
import soundfile as sf

print("="*60)
print("AUDIO AUFNAHME")
print("="*60)
print("Spreche 30 Sekunden lang Deutsch...")
print("Die Aufnahme startet in 3 Sekunden...\n")

import time
for i in range(3, 0, -1):
    print(f"  {i}...")
    time.sleep(1)

duration = 30  # 30 Sekunden
sample_rate = 16000

print("Aufnahme läuft...")
audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32')
sd.wait()

# Speichere als test.mp3
sf.write('test.mp3', audio, sample_rate)
print("\n✓ Gespeichert: test.mp3")

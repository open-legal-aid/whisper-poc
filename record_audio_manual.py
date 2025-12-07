import sounddevice as sd
import soundfile as sf

print("="*60)
print("AUDIO AUFNAHME")
print("="*60)
print("Spreche Deutsch...")
print("Drücke ENTER um die Aufnahme zu STOPPEN\n")

sample_rate = 16000

# Aufnahme starten
print("Aufnahme läuft...")
audio_list = []

def audio_callback(indata, frames, time_info, status):
    if status:
        print(status)
    audio_list.append(indata.copy())

# Stream für Live-Recording
stream = sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate)

with stream:
    input("Drücke ENTER zum Stoppen...")

# Audio zusammenfassen
import numpy as np
audio = np.concatenate(audio_list, axis=0)

# Speichere
sf.write('test.mp3', audio, sample_rate)
print(f"\n✓ Gespeichert: test.mp3 ({len(audio)/sample_rate:.1f} Sekunden)")

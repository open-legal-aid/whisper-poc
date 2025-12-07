import os
import whisper
from pathlib import Path

# Pfad setzen
models_path = Path('./models/whisper')
models_path.mkdir(parents=True, exist_ok=True)
os.environ['WHISPER_CACHE'] = str(models_path)

print(f"\n{'='*60}")
print(f"Lade Whisper Modelle...")
print(f"Pfad: {models_path}")
print(f"{'='*60}\n")

# Medium laden
print("Lade MEDIUM Modell (~1.5 GB)...")
try:
    model_medium = whisper.load_model('medium')
    print("✓ Medium erfolgreich geladen!\n")
except Exception as e:
    print(f"✗ Fehler beim Medium: {e}\n")

# Large laden
print("Lade LARGE Modell (~2.9 GB)...")
try:
    model_large = whisper.load_model('large')
    print("✓ Large erfolgreich geladen!\n")
except Exception as e:
    print(f"✗ Fehler beim Large: {e}\n")

# Überprüfe was heruntergeladen wurde
print(f"{'='*60}")
print("Überprüfung:")
print(f"{'='*60}")
for file in sorted(models_path.glob('*.pt')):
    size_mb = file.stat().st_size / (1024**2)
    print(f"✓ {file.name}: {size_mb:.2f} MB")
print()

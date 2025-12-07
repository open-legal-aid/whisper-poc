import os
import whisper
from pathlib import Path

# Pfad explizit setzen
models_dir = r'C:\whisper-poc\models\whisper'
Path(models_dir).mkdir(parents=True, exist_ok=True)

# Umgebungsvariable setzen
os.environ['WHISPER_CACHE'] = models_dir

print(f"\n{'='*60}")
print("Lade Whisper Modelle...")
print(f"Pfad: {models_dir}")
print(f"{'='*60}\n")

# Medium
print("Lade MEDIUM Modell (~1.5 GB)...")
try:
    model_med = whisper.load_model('medium', download_root=models_dir)
    print("✓ Medium erfolgreich geladen!\n")
except Exception as e:
    print(f"✗ Fehler: {e}\n")

# Large
print("Lade LARGE Modell (~2.9 GB)...")
try:
    model_large = whisper.load_model('large', download_root=models_dir)
    print("✓ Large erfolgreich geladen!\n")
except Exception as e:
    print(f"✗ Fehler: {e}\n")

# Überprüfung
print(f"{'='*60}")
print("Überprüfung:")
print(f"{'='*60}")
for file in sorted(Path(models_dir).glob('*.pt')):
    size_mb = file.stat().st_size / (1024**2)
    print(f"✓ {file.name}: {size_mb:.1f} MB")
print()
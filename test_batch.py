import os
from pathlib import Path

os.environ['WHISPER_CACHE'] = r'C:\whisper-poc\models\whisper'

import whisper

model = whisper.load_model('medium')

# Suche alle Audio-Dateien
audio_extensions = ['.mp3', '.wav', '.m4a', '.flac', '.ogg']
audio_dir = Path(r'C:\whisper-poc\audio')  # Erstelle diesen Ordner & pack Audio rein

if audio_dir.exists():
    audio_files = [f for f in audio_dir.glob('*') if f.suffix.lower() in audio_extensions]
    
    if audio_files:
        print(f"Gefunden: {len(audio_files)} Audio-Dateien\n")
        
        for audio_file in audio_files:
            print(f"Transkribiere: {audio_file.name}")
            result = model.transcribe(str(audio_file), language='de')
            
            # Speichere Ergebnis
            output_file = audio_file.with_suffix('.txt')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result['text'])
            
            print(f"  → Gespeichert: {output_file.name}\n")
    else:
        print(f"❌ Keine Audio-Dateien in {audio_dir} gefunden")
else:
    print(f"❌ Ordner {audio_dir} existiert nicht")
    print(f"   Erstelle: {audio_dir}")
    audio_dir.mkdir(parents=True, exist_ok=True)

import os
os.environ['WHISPER_CACHE'] = r'C:\whisper-poc\models\whisper'

import whisper

# Audio-Dateien testen (mp3, wav, m4a, etc.)
audio_file = "test.mp3"  # Ändere je nach Datei

if not os.path.exists(audio_file):
    print(f"❌ {audio_file} nicht gefunden!")
    print("📝 Bitte eine Audio-Datei im whisper-poc Ordner speichern")
else:
    print(f"Lade Modell...")
    model = whisper.load_model('medium')
    
    print(f"\nTranskribiere: {audio_file}")
    result = model.transcribe(audio_file, language='de')
    
    print("\n" + "="*60)
    print("TRANSKRIPTION:")
    print("="*60)
    print(result['text'])
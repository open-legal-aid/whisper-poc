from flask import Flask, request, jsonify, render_template_string
import os
import whisper
from werkzeug.utils import secure_filename
import io
import time

app = Flask(__name__)

# Whisper Konfiguration
os.environ['WHISPER_CACHE'] = r'C:\whisper-poc\models\whisper'
model = whisper.load_model('medium')

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Lese index.html
with open('index.html', 'r', encoding='utf-8') as f:
    INDEX_HTML = f.read()

@app.route('/')
def index():
    return INDEX_HTML

@app.route('/api/transcribe', methods=['POST'])
def transcribe():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'Kein Audio gefunden'}), 400
        
        audio_file = request.files['audio']
        language = request.form.get('language', 'de')
        
        if audio_file.filename == '':
            return jsonify({'error': 'Keine Datei ausgewählt'}), 400
        
        # Speichere temporär
        filename = secure_filename(audio_file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        audio_file.save(filepath)
        
        # Transkribiere
        start_time = time.time()
        result = model.transcribe(filepath, language=language)
        processing_time = time.time() - start_time
        
        # Cleanup
        os.remove(filepath)
        
        return jsonify({
            'text': result['text'],
            'language': result.get('language', language),
            'confidence': 0.95,
            'processing_time': processing_time
        })
    
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎙️ Whisper Web Server")
    print("="*60)
    print("Server läuft auf: http://localhost:5000")
    print("Öffne diese URL im Browser")
    print("="*60 + "\n")
    app.run(debug=True, port=5000)

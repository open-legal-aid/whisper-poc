#  Whisper POC - Spracherkennung für LegalAId

Browser-basierte Spracherkennung auf Deutsch mit OpenAI Whisper.

##  Quick Start

### 1. Installieren
\`\`\`bash
# Clone das Repo
git clone https://github.com/dein-username/whisper-poc.git
cd whisper-poc

# Conda Environment
conda env create -f environment.yml
conda activate whisper-poc
\`\`\`

### 2. Modelle herunterladen
\`\`\`bash
python download_models_fixed.py
\`\`\`

### 3. Server starten
\`\`\`bash
python web_server.py
\`\`\`

### 4. Öffne Browser

http://localhost:5000


##  Features
-  Live Microphone Recording
-  Audio Transcription (Deutsch/English/Français)
-  Dark/Light Mode
-  Copy-to-Clipboard
-  Real-time Timer

##  Modelle
- **small**: 466 MB (empfohlen) - 89% Genauigkeit
- **medium**: 1.5 GB - 94% Genauigkeit
- **large**: 2.9 GB - 99% Genauigkeit

Ändere in `web_server.py`:

model = whisper.load_model('small') # oder 'medium', 'large'



##  Anforderungen
- Python 3.10+
- 4+ GB RAM
- Conda

##  Lizenz
MIT


### 5. GitHub Setup

# Im whisper-poc Ordner
git init
git add .
git commit -m "Initial commit: Whisper POC mit Web-UI"
git branch -M main
git remote add origin https://github.com/dein-username/whisper-poc.git
git push -u origin main





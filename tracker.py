import os
import pyaudio
from pocketsphinx import LiveSpeech, get_model_path

# Festlegen der Spracherkennungsmodelldatei und der erforderlichen Konfigurationsdateien
model_path = get_model_path()
config = {
    'verbose': False,
    'audio_file': None,
    'buffer_size': 2048,
    'no_search': False,
    'full_utt': False,
    'hmm': os.path.join(model_path, 'en-us'),
    'lm': os.path.join(model_path, 'en-us.lm.bin'),
    'dict': os.path.join(model_path, 'cmudict-en-us.dict')
}

# Festlegen der Anfangswerte für den Score und die Anzahl der Schläge
score = 0
num_hits = 0

# Funktion zum Verarbeiten von Sprachbefehlen
def process_speech(phrase):
    global score, num_hits
    if "add" in phrase and "point" in phrase:
        score += 1
        num_hits += 1
        print("Punkt hinzugefügt. Gesamtpunktzahl: ", score)
    elif "subtract" in phrase and "point" in phrase:
        score -= 1
        num_hits += 1
        print("Punkt abgezogen. Gesamtpunktzahl: ", score)
    elif "reset" in phrase and "score" in phrase:
        score = 0
        num_hits += 1
        print("Score zurückgesetzt. Gesamtpunktzahl: ", score)

# Einrichten des LiveSpeech-Objekts zum Empfangen von Sprachbefehlen
speech = LiveSpeech(**config)
for phrase in speech:
    # Nur die ersten 5 Schläge verarbeiten
    if num_hits < 5:
        print("Spracherkennungsergebnis:", phrase)
        process_speech(str(phrase))
    else:
        break

import os
import speech_recognition as sr
from pydub import AudioSegment

def convert_to_wav(audio_path):
    try:
        audio = AudioSegment.from_file(audio_path)
        wav_path = os.path.splitext(audio_path)[0] + ".wav"
        audio.export(wav_path, format="wav")
        return wav_path
    except Exception as e:
        print(f"Error al convertir el archivo: {e}")
        return None

def transcribe_audio(audio_path, language="es-ES"):
    recognizer = sr.Recognizer()
    if not audio_path.endswith(".wav"):
        print("Convirtiendo archivo a WAV...")
        audio_path = convert_to_wav(audio_path)
        if not audio_path:
            return None
    try:
        with sr.AudioFile(audio_path) as source:
            print("Transcribiendo audio...")
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data, language=language)
            return transcription
    except Exception as e:
        print(f"Error al transcribir: {e}")
        return None

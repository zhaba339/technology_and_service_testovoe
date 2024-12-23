import speech_recognition as sr
from fastapi import FastAPI

def recognize():
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile("audio/test_audio.wav")
    with audio_file as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_vosk(audio_data)
        print(text)


app = FastAPI()

@app.post('/asr')
async def asr():
    return recognize()


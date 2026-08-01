import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import uuid
import os

def voice_input(lang):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=lang)
        return text
    except:
        return "Sorry, could not understand"

def voice_output(text, lang):
    filename = f"audio_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

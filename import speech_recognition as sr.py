import speech_recognition as sr
from gtts import gTTS
import os
import time


r = sr.Recognizer()


def listen_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-RU')
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            print("Could not request results; check your internet connection")
            return None


def manipulate_text(text):
    return f"Вы сказали: {text}"


def text_to_speech(text):
    tts = gTTS(text=text, lang='ru')
    tts.save("response.mp3")
    os.system("start response.mp3")


wake_word = "маруся"
print("Assistant is listening for the wake word...")

while True:
    print("Listening for wake word...")
    text = listen_speech()
    if text and wake_word in text.lower():
        print("Wake word detected. What is your request?")
        time.sleep(1)  
        command_text = listen_speech()
        if command_text:
            response_text = manipulate_text(command_text)
            text_to_speech(response_text)

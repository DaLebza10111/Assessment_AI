import openai
from google.cloud import speech_v1p1beta1 as speech
import pyttsx3
import speech_recognition as sr
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def initialize_tts():
    tts_engine = pyttsx3.init()
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        if "en_US" in voice.id or "English" in voice.id:  
            tts_engine.setProperty('voice', voice.id)
            break
    tts_engine.setProperty('rate', 170)  
    tts_engine.setProperty('volume', 1.0) 
    return tts_engine

tts_engine = initialize_tts()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def transcribe_audio(audio_data):
    client = speech.SpeechClient()
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )
    audio = speech.RecognitionAudio(content=audio_data)

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        return result.alternatives[0].transcript

def capture_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return None
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return None

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an IELTS instructor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    print("Initializing IELTS Instructor Program...")
    speak("Hello, I am your IELTS instructor. Let's have a conversation to help you improve your English speaking skills.")

    while True:
        user_input = capture_audio()
        if user_input:
            print(f"You: {user_input}")

            gpt_response = chat_with_gpt(user_input)
            print(f"IELTS Instructor: {gpt_response}")

            speak(gpt_response)

if __name__ == "__main__":
    main()

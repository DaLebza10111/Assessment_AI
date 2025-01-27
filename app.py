import openai
from google.cloud import speech_v1p1beta1 as speech
import pyttsx3
import speech_recognition as sr
import os
from fpdf import FPDF
from datetime import datetime

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

def save_conversation_to_pdf(conversation):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"conversation_{timestamp}.pdf"

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="IELTS Instructor Conversation", ln=True, align='C')
        pdf.ln(10)

        for entry in conversation:
            role, text = entry
            pdf.set_font("Arial", style='B', size=12)
            pdf.cell(0, 10, txt=f"{role}:", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text)
            pdf.ln(5)

        pdf.output(filename)
        print(f"Conversation saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the conversation: {e}")

def provide_feedback(response):
    feedback = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Provide detailed feedback on grammatical range, accuracy, and pronunciation for IELTS speaking responses."},
            {"role": "user", "content": response}
        ]
    )
    return feedback['choices'][0]['message']['content']

def practice_mode():
    conversation = []
    print("Entering Practice Mode...")
    speak("Practice mode started. Please speak your response, and I will provide instant feedback.")

    while True:
        user_input = capture_audio()
        if user_input:
            if user_input.lower() in ["exit", "quit", "stop"]:
                print("Ending Practice Mode...")
                speak("Ending practice mode. Goodbye!")
                break

            print(f"You: {user_input}")
            conversation.append(("You", user_input))

            feedback = provide_feedback(user_input)
            print(f"Feedback: {feedback}")
            conversation.append(("Feedback", feedback))

            speak(feedback)

    save_conversation_to_pdf(conversation)

def test_mode():
    conversation = []
    print("Entering Test Mode...")
    speak("Test mode started. Let us begin the IELTS speaking test. There are three parts.")

    # Part 1: Introduction
    speak("Part 1: Introduction. Please tell me about yourself.")
    user_input = capture_audio()
    if user_input:
        print(f"You: {user_input}")
        conversation.append(("Part 1", user_input))

    # Part 2: Long Turn (Cue Card Activity)
    speak("Part 2: Long Turn. Here is your cue card: Describe a person who has influenced you. You have one minute to think and then speak for up to two minutes.")
    print("(Simulating one minute of preparation time...)")
    speak("Please start now.")
    user_input = capture_audio()
    if user_input:
        print(f"You: {user_input}")
        conversation.append(("Part 2", user_input))

    speak("Part 3: Two-Way Discussion. Let's discuss related topics. Why do you think people look up to role models?")
    user_input = capture_audio()
    if user_input:
        print(f"You: {user_input}")
        conversation.append(("Part 3", user_input))

    speak("Thank you for completing the test. Here is your feedback.")
    for part, response in conversation:
        feedback = provide_feedback(response)
        print(f"Feedback for {part}: {feedback}")
        conversation.append((f"Feedback for {part}", feedback))
        speak(feedback)

    save_conversation_to_pdf(conversation)

def main():
    print("Initializing IELTS Instructor Program...")
    speak("Welcome to the IELTS instructor program. Please choose a mode: Practice or Test.")

    while True:
        speak("Say 'Practice' for Practice Mode or 'Test' for Test Mode. Say 'Exit' to quit.")
        mode = capture_audio()

        if mode:
            mode = mode.lower()
            if mode == "practice":
                practice_mode()
            elif mode == "test":
                test_mode()
            elif mode in ["exit", "quit", "stop"]:
                print("Exiting the program...")
                speak("Goodbye! It was nice talking to you. Goodbye!")
                break
            else:
                print("Invalid mode. Please say 'Practice' or 'Test'.")
                speak("Invalid choice. Please say 'Practice' or 'Test'.")

if __name__ == "__main__":
    main()

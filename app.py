import openai
import pyaudio
import wave
import os
import io
from google.cloud import speech
from gtts import gTTS
from playsound import playsound

# Initialize OpenAI API
openai.api_key = "your_openai_api_key"

# Google Speech-to-Text setup
speech_client = speech.SpeechClient()

# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5  # Length of each speech input
WAVE_OUTPUT_FILENAME = "output.wav"

def record_audio(filename):
    """Record audio from microphone."""
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording complete.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def transcribe_audio(filename):
    """Transcribe audio to text using Google Speech-to-Text."""
    with io.open(filename, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code="en-US",
    )

    response = speech_client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript

    return None

def generate_response(prompt):
    """Generate a response from OpenAI."""
    response = openai.ChatCompletion.create(
        model="chatgpt-4o-realtime-preview-2024-12-17",
        messages=[
            {"role": "system", "content": "You are an IELTS instructor helping the user practice English speaking skills."},
            {"role": "user", "content": prompt},
        ]
    )
    return response['choices'][0]['message']['content']

def text_to_speech(text, output_file="response.mp3"):
    """Convert text to speech using Google Text-to-Speech."""
    tts = gTTS(text)
    tts.save(output_file)
    playsound(output_file)
    os.remove(output_file)

def main():
    print("Welcome to the IELTS speaking practice!")
    print("Press Ctrl+C to exit.")

    while True:
        try:
            # Record user input
            record_audio(WAVE_OUTPUT_FILENAME)

            # Transcribe audio to text
            user_input = transcribe_audio(WAVE_OUTPUT_FILENAME)
            if user_input:
                print(f"You said: {user_input}")

                # Get response from OpenAI
                response = generate_response(user_input)
                print(f"IELTS Instructor: {response}")

                # Speak the response
                text_to_speech(response)
            else:
                print("Could not understand audio. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting. Goodbye!")
            break

if __name__ == "__main__":
    main()

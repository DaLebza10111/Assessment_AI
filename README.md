This program uses Python to create a conversational IELTS instructor application. It helps users get better at speaking English by simulating an IELTS instructor's conversation using OpenAI's GPT-4. The system employs text-to-speech (TTS) to give verbal feedback and speech recognition to record user input. Speaking via a microphone allows the user to communicate with the software; the application will react according to the dialogue with the GPT model.

Getting started:
    Create a Virtual Environment (Optional but Recommended) - python3 -m venv <environment_name>
    Activate your virtual environment [This step may vary depending on whether you use macbook or windows laptop]
    Install Dependencies - pip install -r requirements.txt
    run the program - python main.py [after typing press Enter]

Dependencies:
openai: For interacting with OpenAI's GPT-4 model.
pyttsx3: For text-to-speech functionality (allows the program to speak).
speech_recognition: For converting speech into text.
google-cloud-speech: To transcribe speech using Google Cloud Speech-to-Text API.
os: To manage environment variables, such as the OpenAI API key.

Challenges:
Time lag between the prompts and response.
Limited access (developer/free-tier).

Nice to haves:
Able to end conversation whenever the user wants to.
Continuous listening while the AI is responding to previous prompt.
Shorter pause breaks [premium/paid api version].
Ability to choose between different voices/accents.

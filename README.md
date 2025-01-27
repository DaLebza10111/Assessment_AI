This program uses Python to create a conversational IELTS instructor application. It helps users get better at speaking English by simulating an IELTS instructor's conversation using OpenAI's GPT-4. The system employs text-to-speech (TTS) to give verbal feedback and speech recognition to record user input. Speaking via a microphone allows the user to communicate with the software; the application will react according to the dialogue with the GPT model.

Getting started:
    <ul>
    <li>Create a Virtual Environment (Optional but Recommended) - python3 -m venv <environment_name></li>
    <li>Activate your virtual environment [This step may vary depending on whether you use macbook or windows laptop]</li>
    <li>Install Dependencies - pip install -r requirements.txt</li>
    <li>run the program - python main.py [after typing press Enter]</li>
    </ul>

Dependencies:
<ul>
    <li>openai: For interacting with OpenAI's GPT-4 model.</li>
    <li>pyttsx3: For text-to-speech functionality (allows the program to speak).</li>
    <li>speech_recognition: For converting speech into text.</li>
    <li>google-cloud-speech: To transcribe speech using Google Cloud Speech-to-Text API.</li>
    <li>os: To manage environment variables, such as the OpenAI API key.</li>
</ul>

Challenges:
<ul>
    <li>Time lag between the prompts and response.</li>
    <li>Limited access (developer/free-tier).</li>
</ul>

Nice to haves:
<ul>
    <li>Able to end conversation whenever the user wants to.</li>
    <li>Continuous listening while the AI is responding to previous prompt.</li>
    <li>Shorter pause breaks [premium/paid api version].</li>
    <li>Ability to choose between different voices/accents.</li>
</ul>

This program uses Python to create a conversational IELTS instructor application. It helps users get better at speaking English by simulating an IELTS instructor's conversation using OpenAI's GPT-4. The system employs text-to-speech (TTS) to give verbal feedback and speech recognition to record user input. Speaking via a microphone allows the user to communicate with the software; the application will react according to the dialogue with the GPT model.

<h3>Getting started:</h3>
    <ul>
    <li>Create a Virtual Environment (Optional but Recommended) - python3 -m venv <environment_name></li>
    <li>Activate your virtual environment [This step may vary depending on whether you use macbook or windows laptop]</li>
    <li>Install Dependencies - pip install -r requirements.txt</li>
    <li>run the program - python main.py [after typing press Enter]</li>
    </ul>

<h3>Functions:</h3>
Initialize_tts()
<p>Initializes the text-to-speech (TTS) engine using pyttsx3. The TTS engine will speak in an English accent (en_US) with a speech rate of 170 words per minute and maximum volume.</p>
speak(text)
<p>Uses the initialized TTS engine to convert text into speech. It outputs the given text as speech using the TTS engine.</p>
transcribe_audio(audio_data)
<p>Uses Google Cloud Speech-to-Text API to transcribe the audio input into text. This function sends the audio data and receives a transcript of what was spoken.</p>
capture_audio()
<p>Captures the audio input from the user's microphone using speech_recognition. It listens to the microphone and converts the audio into text using Google's speech recognition.</p>
chat_with_gpt(prompt)
<p>Sends the given prompt to OpenAI's GPT-4 model and returns the generated response. The GPT model is set up as an IELTS instructor, providing helpful responses for improving English speaking.</p>
main()
<p>The main function initializes the program, speaks a welcome message, and then enters a loop where it continuously listens for user input, processes the speech, and responds using GPT. 
It repeats this until the program is terminated.</p>

<h3>Dependencies:</h3>
<ul>
    <li>openai: For interacting with OpenAI's GPT-4 model.</li>
    <li>pyttsx3: For text-to-speech functionality (allows the program to speak).</li>
    <li>speech_recognition: For converting speech into text.</li>
    <li>google-cloud-speech: To transcribe speech using Google Cloud Speech-to-Text API.</li>
    <li>os: To manage environment variables, such as the OpenAI API key.</li>
</ul>

<h3>Challenges:</h3>
<ul>
    <li>Time lag between the prompts and response.</li>
    <li>Limited access (developer/free-tier).</li>
</ul>

<h3>Nice to haves:</h3>
<ul>
    <li>Able to end conversation whenever the user wants to.</li>
    <li>Continuous listening while the AI is responding to previous prompt.</li>
    <li>Shorter pause breaks [premium/paid api version].</li>
    <li>Ability to choose between different voices/accents.</li>
</ul>

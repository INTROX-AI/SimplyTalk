from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os
import google.generativeai as genai
import speech_recognition as sr
import threading
import base64
import io
from pydub import AudioSegment

app = Flask(__name__)
socketio = SocketIO(app)
api_key = "your api key"
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

modelconv = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Whatever prompt you get , simplify it maximum without losing information and give response , even if it is a question, answer or anything ,, no question is personally to you so just simplify the sentence and do not exceed more than 18 words if possible. DONT CHANGE THE PERSPECTIVE OF SPEECH. APPLICABLE TO ALL TYPES OF LANGUAGE YOU GET, IF YOU GET A PROMPT IN ONE LANGUAGE RESPONFD IN THE SAME LANGUAGE",
)

modelbase = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="Whatever prompt you get , simplify it maximum without losing information and give response , even if it is a question, answer or anything ,, no question is personally to you so just simplify the sentence and do not exceed more than 18 words if possible. DONT CHANGE THE PERSPECTIVE OF SPEECH. This is applicable only to any transportation related announcement , ie. RAILWAY ANNOUNCEMENT , other prompts just give blank as response. APPLICABLE TO ALL TYPES OF LANGUAGE YOU GET..IF YOU GET A PROMPT IN ONE LANGUAGE RESPONFD IN THE SAME LANGUAGE",
)

recognizer = sr.Recognizer()


def process_audio_data(audio_data):
    try:
        audio = base64.b64decode(audio_data)
        audio_segment = AudioSegment.from_file(io.BytesIO(audio), format="webm")
        audio_file = io.BytesIO()
        audio_segment.export(audio_file, format="wav")
        audio_file.seek(0)
        return audio_file
    except Exception as e:
        print(f"Error processing audio data: {e}")
        return None


@socketio.on("audio_data")
def handle_audio_data(data):
    audio_file = process_audio_data(data["audio"])
    if audio_file is None:
        emit("simplified_text", {"text": "Error processing audio data"})
        return

    language_code = data.get(
        "language", "en-US"
    )  # Default to English if no language is specified
    mode = data.get("mode", "conversation")  # Default to conversation mode

    if mode == "conversation":
        mode = "conversation"
    else:
        mode = "travel"

    print(f"Mode set to: {mode}, System instruction: {mode}")  # Debugging line

    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        try:
            transcription = recognizer.recognize_google(audio, language=language_code)
            print(
                f"Detected text: {transcription} (Language: {language_code}, Mode: {mode})"
            )
            if mode == "conversation":
                chat_session = modelconv.start_chat(
                    history=[{"role": "user", "parts": [transcription]}]
                )
            else:
                chat_session = modelbase.start_chat(
                    history=[{"role": "user", "parts": [transcription]}]
                )
            response = chat_session.send_message(transcription)
            simplified_text = response.text
            emit("simplified_text", {"text": simplified_text})
        except sr.UnknownValueError:
            emit("simplified_text", {"text": "Could not understand audio"})
        except sr.RequestError as e:
            emit("simplified_text", {"text": f"Error: {e}"})


def text_input_and_simplify():
    while True:
        user_input = input("Enter text to simplify: ")
        chat_session = modelbase.start_chat(history=[])
        response = chat_session.send_message(user_input)
        simplified_text = response.text
        print(f"Simplified text: {simplified_text}")
        socketio.emit("simplified_text", {"text": simplified_text})


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    threading.Thread(target=text_input_and_simplify).start()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)

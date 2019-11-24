from flask import Flask, request
from TextToSpeech import tts
import json

app = Flask(__name__)

@app.route("/ping")
def home():
    return "Pong!"

@app.route("/getText", methods=["POST"])
def salvador():
    resp = request.get_json()
    response = resp["bear_text"]
    speak(response)
	# DO stuff here
    return "Success"

def speak(response):
    speech = tts()
    speech.say(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0")


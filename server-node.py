from flask import Flask, request
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

# Configuración de Gotify
GOTIFY_URL = "https://gotify.yourserver.com"
GOTIFY_TOKEN = "YourGotifyToken"
last_seen = datetime.now()


def notify_gotify(message):
    url = f"{GOTIFY_URL}/message?token={GOTIFY_TOKEN}"
    data = {"title": "NodeMCU Status", "message": message, "priority": 5}
    response = requests.post(url, json=data)
    return response.text


@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    global last_seen
    last_seen = datetime.now()
    return "Heartbeat received"


@app.before_first_request
def activate_job():
    def run_job():
        global last_seen
        while True:
            time.sleep(300)  # Wait for 5 minutes
            if datetime.now() > last_seen + timedelta(minutes=5):
                message = "NodeMCU is offline!"
                notify_gotify(message)
                print(message)

    from threading import Thread

    thread = Thread(target=run_job)
    thread.start()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

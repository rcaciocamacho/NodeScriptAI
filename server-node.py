from flask import Flask, request
import requests
from telegram import Bot

app = Flask(__name__)
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
bot = Bot(token=TELEGRAM_TOKEN)


@app.route("/request_chatgpt", methods=["GET"])
def handle_request():
    prompt = "¿Qué hora es y cómo está el tiempo en Madrid?"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "text-davinci-003",  # Use an appropriate model
        "prompt": prompt,
        "max_tokens": 100,
    }
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        json=data,
        headers=headers,
    )
    result = response.json()["choices"][0]["text"].strip()
    bot.send_message(chat_id=CHAT_ID, text=result)
    return f"Mensaje enviado a Telegram: {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

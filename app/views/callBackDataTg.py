from flask import request
import telebot

from app import app, bot

@app.route('/callback_data_tg', methods=["POST"])
def callbackDataTelegram():
    data = request.json
    bot.send_message(text="123", chat_id="5693374811")
    if request.headers.get('content-type') == 'application/json':
        update = telebot.types.Update.de_json(data)
        bot.process_new_updates([update])
        return {"ok":True}
    else:
        return {"ok":False}

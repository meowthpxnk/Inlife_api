from flask import request
import telebot

from app import app, bot

@app.route('/callback_data_tg', methods=["POST"])
def callbackDataTelegram():
    data = request.json
    if request.headers.get('content-type') == 'application/json':
        update = telebot.types.Update.de_json(data)
        bot.process_new_updates([update])
        return {"ok":True}
    else:
        return {"ok":False}


# from app import admin

# @app.route('/tg_admin_info', methods=["GET"])
# def tg_admin_info():
#     try:
#         return {
#             "info": f"{admin.state}"
#         }
#     except Exception as e:
#         return {
#             "error": e
#         }
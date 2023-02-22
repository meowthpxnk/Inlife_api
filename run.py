from app import app, db, bot
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # app.run(host="192.168.1.80")
        bot.send_message(text="123", chat_id="5693374811")
        bot.set_webhook(url="https://api.arcadakms.ru/callback_data_tg")
        app.run()

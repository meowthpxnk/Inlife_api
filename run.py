from app import app, db, bot
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # app.run(host="192.168.1.80")
        bot.set_webhook(url="https://api.arcadakms.ru/callback_data_tg")
        app.run()

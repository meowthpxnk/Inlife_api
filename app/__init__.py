import os

import telebot

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


app = Flask(__name__)

TOKEN = "5855595896:AAHdnmM-u0PXDAsf0J3N5SbFJIaTIknfpC0"
bot = telebot.TeleBot(TOKEN)


CORS(app)
cors = CORS(app, resources = {
    r"*":{
        "origins": "*"
    }
})

app.config.from_object('app.config.Config')

app_ctx = app.app_context()
app_ctx.push()

db = SQLAlchemy(app)

Migrate(app, db)
from app import views, models




from tg_admin.admin_pannel import TgAdmin

admin = TgAdmin(5693374811)

from tg_admin import message_handlers

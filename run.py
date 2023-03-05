from app import app, db, bot

from app.models import MenuDishSecond
from test import createDishSecond, createDish
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()
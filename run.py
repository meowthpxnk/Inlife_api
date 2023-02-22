from app import app
from app import db
import os

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host="192.168.1.80")
        # app.run()

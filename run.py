from app import app, db
from test import getPhotoReports

if __name__ == '__main__':
    print(getPhotoReports())
    with app.app_context():
        db.create_all()
        app.run()
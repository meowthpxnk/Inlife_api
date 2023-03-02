from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    date = db.Column(db.DateTime)

    def __init__(self, title=None, img=None, date=None, description=None):
        self.title = title
        self.img = img
        self.date = date
        self.description = description

    def info(self):
        return {
            "id": self.id,
            "title": self.title,
            "date_time": self.date,
            "date": "12 ОКТ",
            "img": self.img,
        }

    def getFullInfo(self):
        return {
            "id": self.id,
            "title": self.title,
            "date_time": self.date,
            "date": "12 октября",
            "img": self.img,
            "description": self.description,
        }

    @classmethod
    def findById(cls, id):
        item = db.session.query(cls).filter(cls.id == id).first()

        if not item:
            raise Exception("Not existed")

        return item

    @classmethod
    def allItems(cls):
        return db.session.query(cls).all()

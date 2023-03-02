from app import db

class PhotoReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    img = db.Column(db.String)
    date = db.Column(db.DateTime)
    photos = db.relationship('Photo', backref='PhotoReport')

    def __init__(self, title=None, img=None, date=None):
        self.title = title
        self.img = img
        self.date = date

    def info(self):
        # print(self.photos)
        return {
            "id": self.id,
            "title": self.title,
            "img": self.img,
            "date_time": self.date,
            "date": "12.04.2022",
            "photos_quantity": len(self.photos),
        }

    def getFullInfo(self):
        return {
            "date_time": self.date,
            "date": "12/02/12",
            "title": self.title,
            "photos": [{"img": photo.img} for photo in self.photos],
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

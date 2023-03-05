from app import db

class MenuCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String)
    title = db.Column(db.String)

    semi_categories = db.relationship('MenuDish', backref='MenuCategory')

    def __init__(self, img=None, title=None):
        self.img = img
        self.title = title

    def info(self):
        return {
            "id": self.id,
            "img": self.img,
            "title": self.title,
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

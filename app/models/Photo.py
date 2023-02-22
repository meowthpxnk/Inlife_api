from app import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String)
    photo_report_id = db.Column(db.Integer, db.ForeignKey('photo_report.id'))

    def __init__(self, photo_report_id, img=None):
        self.img = img
        self.photo_report_id = photo_report_id

    @classmethod
    def findById(cls, id):
        item = db.session.query(cls).filter(cls.id == id).first()

        if not item:
            raise Exception("Not existed")

        return item

    @classmethod
    def allItems(cls):
        return db.session.query(cls).all()

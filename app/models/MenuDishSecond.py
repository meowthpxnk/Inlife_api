from app import db

class MenuDishSecond(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String)
    price = db.Column(db.String)
    portion = db.Column(db.String)
    ingredients = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey('menu_dish.id'))

    def __init__(self, category_id, title=None, price=None, portion=None, ingredients=None):
        self.title = title
        self.price = price
        self.portion = portion
        self.ingredients = ingredients

        self.category_id = category_id

    def info(self):
        return {
            "title": self.title,
            "price": self.price,
            "portion": self.portion,
            "ingredients": self.ingredients,
            # "category_id": self.category_id,
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

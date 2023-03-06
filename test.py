from app.models import Event, MenuCategory, MenuDish, MenuDishSecond, PhotoReport, Photo
from app import db
from app import app, bot
import os
from datetime import datetime, timedelta

import requests

import io

from PIL import Image

def openPilImage(url):
    r = requests.get(url, stream=True)
    image = io.BytesIO(r.content)
    return image

def tryCatch(func):
    def tryer(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise Exception(e)
        raise "Unkown error"
    return tryer

def isExistedDirectory(directory):
    return os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], directory))

def createDirectory(directory):
    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], directory))

@tryCatch
def saveImage(image, directory, filename):
    if not isExistedDirectory(directory):
        createDirectory(directory)
    path = os.path.join(app.config['UPLOAD_FOLDER'], directory, filename)
    image.save(path)

@tryCatch
def parseDate(date):
    return datetime.strptime(date, "%d/%m/%Y(%H:%M)")





def createEvent(title, description, image, date):

    errors = []

    try:
        date = parseDate(date)
    except Exception as e:
        errors.append({
            "name": "date",
            "exception_code": "DATE_ERROR",
            "exception": e
        })


    try:
        image = Image.open(image)
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_ERROR",
            "exception": e
        })

    event = Event(title=title, description=description, date=date)
    db.session.add(event)
    db.session.commit()

    try:
        filename = f"{event.id}.png"
        saveImage(image, "events", filename)
        event.img = filename
        db.session.commit()
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_SAVE_ERROR",
            "exception": e
        })

    if not errors:
        return {"errors": False, "event": event}

    db.session.delete(event)
    db.session.commit()
    return {"errors": True, "errors_list": errors}

def createCategory(title, image):
    errors = []


    try:
        image = Image.open(image)
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_ERROR",
            "exception": e
        })

    category = MenuCategory(title=title)
    db.session.add(category)
    db.session.commit()


    try:
        filename = f"{category.id}.png"
        saveImage(image, "categories", filename)
        category.img = filename
        db.session.commit()
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_SAVE_ERROR",
            "exception": e
        })

    if not errors:
        return {"errors": False, "category": category}

    db.session.delete(category)
    db.session.commit()
    return {"errors": True, "errors_list": errors}

def createDish(title, category_id):
    bot.send_message(chat_id="5693374811", text="СОЗДАЮ ЕБАНА")
    errors = []

    try:
        category = MenuCategory.findById(category_id)
    except Exception as e:
        errors.append({
            "name": "category",
            "exception_code": "CATEGORY_NOT_EXISTED",
            "exception": e
        })

    if not errors:
        dish = MenuDish(
            title=title,
            # price=price,
            # portion=portion,
            # ingredients=ingredients,
            category_id=category.id,
        )
        db.session.add(dish)
        db.session.commit()
        return dish

    return {"errors": True, "errors_list": errors}

def createDishSecond(title, price, portion, ingredients, category_id):
    bot.send_message(chat_id="5693374811", text="СОЗДАЮ ЕБАНА")
    errors = []

    try:
        category = MenuDish.findById(category_id)
    except Exception as e:
        errors.append({
            "name": "category",
            "exception_code": "CATEGORY_NOT_EXISTED",
            "exception": e
        })

    if not errors:
        dish = MenuDishSecond(
            title=title,
            price=price,
            portion=portion,
            ingredients=ingredients,
            category_id=category.id,
        )
        db.session.add(dish)
        db.session.commit()
        return dish

    return {"errors": True, "errors_list": errors}

def createPhotoReport(title, image, date):

    errors = []

    try:
        date = parseDate(date)
    except Exception as e:
        errors.append({
            "name": "date",
            "exception_code": "DATE_ERROR",
            "exception": e
        })

    try:
        image = Image.open(image)
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_ERROR",
            "exception": e
        })

    photo_report = PhotoReport(title=title, date=date)
    db.session.add(photo_report)
    db.session.commit()


    try:
        filename = f"{photo_report.id}.png"
        saveImage(image, "photo_reports", filename)
        photo_report.img = filename
        db.session.commit()
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_SAVE_ERROR",
            "exception": e
        })

    if not errors:
        return {"errors": False, "photo_report": photo_report}

    db.session.delete(photo_report)
    db.session.commit()
    return {"errors": True, "errors_list": errors}

def createPhoto(image, photo_report_id):
    errors = []
    try:
        photo_report = PhotoReport.findById(photo_report_id)
    except Exception as e:
        errors.append({
            "name": "photo_report",
            "exception_code": "PHOTO_REPORT_NOT_EXISTED",
            "exception": e
        })

    try:
        image = Image.open(image)
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_ERROR",
            "exception": e
        })

    photo = Photo(photo_report_id = photo_report.id if photo_report else None)
    db.session.add(photo)
    db.session.commit()


    try:
        filename = f"{photo.id}.png"
        saveImage(image, "photos", filename)
        photo.img = filename
        db.session.commit()
    except Exception as e:
        errors.append({
            "name": "image",
            "exception_code": "IMAGE_SAVE_ERROR",
            "exception": e
        })

    if not errors:
        return {"errors": False, "photo": photo}

    db.session.delete(photo)
    db.session.commit()
    return {"errors": True, "errors_list": errors}



def editEvent(event_id, title = None, description = None, image = None, date = None):
    event = Event.findById(event_id)

    if title:
        event.title = title
        db.session.commit()

    if description:
        event.description = description
        db.session.commit()

    if image:
        image = Image.open(image)
        filename = f"{event.id}.png"
        saveImage(image, "events", filename)
        event.img = filename
        db.session.commit()

    if date:
        event.date = parseDate(date)
        db.session.commit()

    return {"errors": False}

def editCategory(category_id, title = None, image = None):
    category = MenuCategory.findById(category_id)

    if title:
        category.title = title
        db.session.commit()

    if image:
        image = Image.open(image)
        filename = f"{category.id}.png"
        saveImage(image, "categories", filename)
        category.img = filename
        db.session.commit()

    return {"errors": False}

def editDish(dish_id, title = None):
    dish = MenuDish.findById(dish_id)

    if title:
        dish.title = title
        db.session.commit()

    # if ingredients:
    #     dish.ingredients = ingredients
    #     db.session.commit()

    # if portion:
    #     dish.portion = portion
    #     db.session.commit()

    # if price:
    #     dish.price = price
    #     db.session.commit()
    

    return {"errors": False}


def editDishSecond(dish_id, title = None, ingredients = None, portion = None, price = None):
    dish = MenuDishSecond.findById(dish_id)

    if title:
        dish.title = title
        db.session.commit()

    if ingredients:
        dish.ingredients = ingredients
        db.session.commit()

    if portion:
        dish.portion = portion
        db.session.commit()

    if price:
        dish.price = price
        db.session.commit()

    return {"errors": False}


def editPhotoReport(photo_report_id, title = None, date = None, image = None):
    photo_report = PhotoReport.findById(photo_report_id)

    if title:
        photo_report.title = title
        db.session.commit()

    if date:
        photo_report.date = parseDate(date)
        db.session.commit()

    if image:
        image = Image.open(image)
        filename = f"{photo_report.id}.png"
        saveImage(image, "photo_reports", filename)
        photo_report.img = filename
        db.session.commit()

    return {"errors": False}


def deleteEvent(id):
    event = Event.findById(id)
    db.session.delete(event)
    db.session.commit()

def deleteCategory(id):
    category = MenuCategory.findById(id)
    db.session.delete(category)
    db.session.commit()

def deleteDish(id):
    dish = MenuDish.findById(id)
    db.session.delete(dish)
    db.session.commit()

def deleteDishSecond(id):
    dish = MenuDishSecond.findById(id)
    db.session.delete(dish)
    db.session.commit()

def deletePhotoReport(id):
    photo_report = PhotoReport.findById(id)
    db.session.delete(photo_report)
    db.session.commit()



def getEventInfos(id):

    try:
        return Event.findById(id).getFullInfo()
    except:
        raise Exception("Not existed Event")

def getPhotoReportInfos(id):

    try:
        return PhotoReport.findById(id).getFullInfo()
    except:
        raise Exception("Not existed photo report")



def getEvents():
    events = db.session.query(Event).filter(Event.date > (datetime.now() - timedelta(days=1))).all()
    return [event.info() for event in events]

def getCategories():
    return [category.info() for category in MenuCategory.allItems()]

def getPhotoReports():
    return [photo_report.info() for photo_report in PhotoReport.allItems()]





def getEventItems():
    return db.session.query(Event).all()

def getDishesItems():
    return db.session.query(MenuDish).all()
    
def getCategoriesItems():
    return db.session.query(MenuCategory).all()

def getSemiCategoriesItems():
    return db.session.query(MenuDishSecond).all()

def getPhotoReportsItems():
    return db.session.query(PhotoReport).all()







def getMenuDishess():
    return [dish.info() for dish in MenuDish.allItems()]

def getMenuDishessSecond():
    return [dish.info() for dish in MenuDishSecond.allItems()]

def getMenuDishesByCategoryID(id):
    category = db.session.query(MenuCategory).filter(MenuCategory.id == id).first()
    semi_categories = category.semi_categories
    print(semi_categories)

    data = []

    for semi_category in semi_categories:
        data.append({
            "title": semi_category.title,
            "dishes": [dish.info() for dish in semi_category.dishes]
        })
    return data

# print(__name__)
if __name__ == "__main__":


    # КАТЕГОРИИ ------------------------- !!!

    # title = "Пиво"
    # image = openPilImage("https://static.insales-cdn.com/files/1/1485/14190029/original/%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D0%B5_%D1%81%D1%82%D0%B8%D0%BB%D0%B5%D0%B9_%D0%BF%D0%B8%D0%B2%D0%B0.jpg")
    #
    # answer = createCategory(
    #     title=title,
    #     image=image,
    # )
    #
    # print(answer)

    # БЛЮДА ------------------------- !!!

    # title = "Крыбовый"
    # price = "2000"
    # portion = "2000 штука"
    # ingredients = "(унакга ыфвфывщзшфыб ывщыфжд влыфждв, dksajd;l , asdjk, колка)"
    # category_id = 4
    #
    # dish = createDish(
    #     title=title,
    #     price=price,
    #     portion=portion,
    #     ingredients=ingredients,
    #     category_id=category_id
    # )
    #
    # print(dish)

    # ФОТО-ОТЧЕТЫ ------------------------- !!!

    # date = "30/12/2024(00:00)"
    # image = openPilImage("https://www.simplilearn.com/ice9/free_resources_article_thumb/what_is_image_Processing.jpg")
    # title = "Кис-кис"
    #
    # photo_report = createPhotoReport(title, image, date)
    # print(photo_report)

    # ФОТО ------------------------- !!!

    # for idx in range(4):
    #     image = openPilImage("https://random.imagecdn.app/500/500")
    #     photo_report_id = 3
    #
    #     photo = createPhoto(image, photo_report_id)
    #     print(photo)

    # МЕРОПРИЯТИЯ ------------------------- !!!

    # image = openPilImage("https://www.pdm.ac.in/wp-pdmu/uploads/2019/10/POSTER-MAKING_page8_image2-233x300.jpg")
    # date = "22/03/2023(12:00)"
    # title = "Egor Letov Вечеринка"
    # description = "Текст фывожыфдловлофды ыфлвыфждлв дфлвшлыфжб !!! ыфозщвлфждылв щ-цлх___-фывоыфлов"


    # event = createEvent(
    #     title = title,
    #     description = description,
    #     date = date,
    #     image = image,
    # )
    # print(image)

    pass

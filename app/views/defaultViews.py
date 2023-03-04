from app import app

import time

from test import getEvents, getEventInfos, getPhotoReports, getCategories, getPhotoReportInfos, getMenuDishess, getMenuDishessSecond

@app.route('/getInlifeInfo', methods=['GET'])
def getInlifeInfo():
    # time.sleep(3)
    return {"ok": True, "data": {
        "menu":{
            "categories": getCategories(),
        },
        "photo_reports":getPhotoReports(),
        "events": getEvents(),
    }}

@app.route('/getEventInfo/<id>', methods=['GET'])
def getEventInfo(id):
    # time.sleep(3)
    return {"ok": True, "data": getEventInfos(id)}


@app.route('/getPhotoReportInfo/<id>', methods=['GET'])
def getPhotoReportInfo(id):
    # time.sleep(3)
    info = getPhotoReportInfos(id)
    print(info)
    return {"ok": True, "data": info}


@app.route('/getMenuDishes', methods=['GET'])
def getMenuDishes():
    # time.sleep(3)
    return {"ok": True, "data": getMenuDishess()}

@app.route('/getMenuDishesSecond', methods=['GET'])
def getMenuDishes():
    # time.sleep(3)
    return {"ok": True, "data": getMenuDishessSecond()}

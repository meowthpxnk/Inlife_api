import os

from flask import send_file

from app import app

upload_folder = os.path.abspath(app.config["UPLOAD_FOLDER"])


@app.route('/images/<directory>/<filename>', methods=['GET'])
def getImage(directory, filename):
    match directory:
        case "events":
            pass
        case "categories":
            pass
        case "photo_reports":
            pass
        case "photos":
            pass
        case _:
            return {"ok": False, "error": "No such directory"}

    try:
        return send_file(os.path.join(upload_folder, directory, filename))
    except:
        return {"ok": False, "error": "No such file"}

    return {"ok": False, "error": "Unknown error"}

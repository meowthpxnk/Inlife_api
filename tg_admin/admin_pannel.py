from app import app, bot
from .admin_states import   CreateEvent, EditEvent, DeleteEvent, \
                            CreateCategory, EditCategory, DeleteCategory, \
                            CreateDish, EditDish, DeleteDish, \
                            CreateDishSecond, EditDishSecond, DeleteDishSecond,\
                            CreatePhotoReport, EditPhotoReport, DeletePhotoReport
 # CreateDish, createCategory

from test import \
    createEvent, createPhotoReport, createPhoto, createCategory, createDish, createDishSecond,\
    editEvent, editCategory, editDish, editPhotoReport, editDishSecond, deleteDishSecond, \
    deleteEvent, deleteCategory, deleteDish, deletePhotoReport

class TgAdmin():
    name = "Lextor"
    chat_id = None
    state = None

    def __init__(self, chat_id):
        self.chat_id = chat_id


    def process_new_updates(self, data, content_type):

        active_step = self.state.active_step()
        if content_type not in active_step.entity_types:
            active_step.send_error()
            return

        if active_step:
            active_step.check_data(data, content_type)


    def send_answer(self, message, reply_markup = None):
        bot.send_message(
            self.chat_id,
            message,
            reply_markup = reply_markup,
            parse_mode = "html"
        )

    def send_start(self):
        self.send_answer("Я запустился")


    def createEvent(self):
        print(self)
        self.state = CreateEvent(self)

    def createDish(self):
        self.state = CreateDish(self)
    
    def createDishSecond(self):
        self.state = CreateDishSecond(self)

    def createCategory(self):
        self.state = CreateCategory(self)

    def createPhotoReport(self):
        self.state = CreatePhotoReport(self)



    def editCategory(self):
        self.state = EditCategory(self)

    def editEvent(self):
        self.state = EditEvent(self)

    def editDish(self):
        self.state = EditDish(self)
    
    def editDishSecond(self):
        self.state = EditDishSecond(self)

    def editPhotoReport(self):
        self.state = EditPhotoReport(self)



    def deleteEvent(self):
        self.state = DeleteEvent(self)

    def deleteCategory(self):
        self.state = DeleteCategory(self)

    def deleteDish(self):
        self.state = DeleteDish(self)
    
    def deleteDishSecond(self):
        self.state = DeleteDishSecond(self)

    def deletePhotoReport(self):
        self.state = DeletePhotoReport(self)


    def generateMethod(self, method_name, data):
        print("---GENERATE_METHOD---")
        self.send_answer("---GENERATE_METHOD---")


        try:
            self.send_answer(f"{method_name = }")
        except Exception as e:
            self.send_answer(f"{e}")
        
        try:
            self.send_answer(f"{str(data)}")
        except Exception as e:
            self.send_answer(f"{e}")


        # print(f"{method_name = }\n{data = }")
        # print("---GENERATE_METHOD---")
        match method_name:
            case "CreateEvent":
                with app.app_context():
                    event = createEvent(
                        title = data["title"],
                        description = data["description"],
                        date = data["date"],
                        image = data["photo"],
                    )
                    print(event)
                return
            case "CreatePhotoReport":
                with app.app_context():
                    photo_report = createPhotoReport(
                        data["title"],
                        data["photo"],
                        data["date"]
                    )
                    print(photo_report)
                    for photo in data["photos"]:
                        photo_report_id = photo_report["photo_report"].id
                        photo = createPhoto(photo, photo_report_id)
                        print(photo)
                return
            case "CreateCategory":
                with app.app_context():
                    category = createCategory(
                        title = data["title"],
                        image = data["photo"],
                    )

                    print(category)
                return
            case "CreateDish":
                with app.app_context():
                    try:
                        dish = createDish(
                            title = data["title"],
                            # price = data["price"],
                            # portion = data["portion"],
                            # ingredients = data['description'],
                            category_id = data['category_id']
                        )
                        # self.send_answer(dish)
                    except Exception as e:
                        self.send_answer(e)

                    print(dish)
                return
            case "CreateDishSecond":
                with app.app_context():
                    try:
                        dish = createDishSecond(
                            title = data["title"],
                            price = data["price"],
                            portion = data["portion"],
                            ingredients = data['description'],
                            category_id = data['category_id']
                        )
                        # self.send_answer(dish)
                    except Exception as e:
                        self.send_answer(e)

                    print(dish)
                return

            case "EditEvent":
                with app.app_context():
                    editEvent(
                        event_id = data.get('id'),
                        title = data.get('title'),
                        description = data.get('description'),
                        image = data.get('photo'),
                        date = data.get('date')
                    )
                return
            case "EditCategory":
                with app.app_context():
                    editCategory(
                        category_id = data.get('id'),
                        title = data.get('title'),
                        image = data.get('photo')
                    )
                return
            case "EditDish":
                with app.app_context():
                    editDish(
                        dish_id = data.get('id'),
                        title = data.get('title'), 
                    )
                return
            case "EditDishSecond":
                with app.app_context():
                    editDishSecond(
                        dish_id = data.get('id'),
                        title = data.get('title'), 
                        ingredients = data.get('description'), 
                        portion = data.get('portion'), 
                        price = data.get('price')
                    )
                return
            case "EditPhotoReport":
                with app.app_context():
                    try:
                        editPhotoReport(
                            photo_report_id = data.get('id'),
                            title = data.get('title'), 
                            date = data.get('date'), 
                            image = data.get('photo')
                        )
                    except Exception as e:
                        self.send_answer(f"{e}")
                return
            

            case "DeleteEvent":
                with app.app_context():
                    if data.get("ok").lower() != 'нет':
                        deleteEvent(
                            id = data.get('id'),
                        )
                return
            case "DeleteCategory":
                with app.app_context():
                    if data.get("ok").lower() != 'нет':
                        deleteCategory(
                            id = data.get('id'),
                        )
                return
            case "DeleteDish":
                with app.app_context():
                    if data.get("ok").lower() != 'нет':
                        deleteDish(
                            id = data.get('id'),
                        )
                return
            case "DeleteDishSecond":
                with app.app_context():
                    if data.get("ok").lower() != 'нет':
                        deleteDishSecond(
                            id = data.get('id'),
                        )
                return
            case "DeletePhotoReport":
                with app.app_context():
                    if data.get("ok").lower() != 'нет':
                        deletePhotoReport(
                            id = data.get('id'),
                        )
                return
            
            
            case _:
                return




    def finish_state(self):
        self.state = None

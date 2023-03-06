from app import bot
from datetime import datetime

from .message_templates import *
from .reply_markups import *

import io
from PIL import Image

class Step:
    message = "asdsad"
    error_message = "step_error"
    entity_types = ["text"]
    name = "default"
    unique_message = None

    data = None
    admin = None
    state = None

    def __init__(self, state, admin, message, error_message, name, reply_markup = None, entity_type = None, unique_message = None):
        self.admin = admin
        self.state = state
        self.message = message
        self.unique_message = unique_message
        self.error_message = error_message
        self.name = name
        self.reply_markup = reply_markup

        self.entity_type = entity_type

    def activate(self):
        if self.message:
            self.admin.send_answer(self.message, reply_markup=self.reply_markup)
        if self.unique_message:
            self.admin.send_answer(self.unique_message())


    def is_current_entity(self, entity_type):
        return entity_type in self.entity_types

    def send_error(self):
        self.admin.send_answer(self.error_message)

    def finish(self):
        self.state.next_step()

    def check_data(self, data, content_type = None):
        try:
            self.parse_data(data, content_type)
            self.finish()
        except Exception as e:
            print(e)
            self.send_error()

    def parse_data(self, data, content_type = None):
        self.data = data

class GetText(Step):
    message = "text"
    entity_types = ["text"]

class GetPhoto(Step):
    message = "photo"
    entity_types = ["photo"]

    def parse_data(self, data, content_type = None):
        self.data = io.BytesIO(data)

class GetDate(Step):
    message = "date"
    entity_types = ["text"]

    def parse_data(self, data, content_type = None):
        parser = datetime.strptime(data, "%d/%m/%Y(%H:%M)")
        self.data = data

class GetNumber(Step):
    message = "number"
    entity_types = ["text"]

    def parse_data(self, data, content_type = None):
        self.data = int(data)

class CirculateStep(Step):
    pass

class EditEventStep(Step):
    entity_types = ["text"]

    def reload(self):
        self.state.steps.append(
            EditEventStep(
                self.state,
                self.admin,
                message = StepMessages.text_edit_event_method,
                error_message = ErrorMessages.text,
                name = "method",
                reply_markup = edit_event_markup,
            )
        )

    def getTitle(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_edit_event_title,
                error_message = ErrorMessages.text,
                name = "title",
                reply_markup = None,
            )
        )

    def getPhoto(self):
        self.state.steps.append(
            GetPhoto(
                self.state,
                self.admin,
                message = StepMessages.text_edit_event_photo,
                error_message = ErrorMessages.photo,
                name = "photo",
                reply_markup = None,
            )
        )

    def getDescription(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_edit_event_description,
                error_message = ErrorMessages.text,
                name = "description",
                reply_markup = None,
            )
        )

    def getDate(self):
        self.state.steps.append(
            GetDate(
                self.state,
                self.admin,
                message = StepMessages.text_edit_event_date,
                error_message = ErrorMessages.date,
                name = "date",
                reply_markup = None,
            )
        )

    def parse_data(self, data, content_type = None):
        self.data = data



        # data = data.low

        match data.lower():
            case "название":
                self.getTitle()
                self.reload()
                return
            case "афиша":
                self.getPhoto()
                self.reload()
                return
            case "описание":
                self.getDescription()
                self.reload()
                return
            case "дата":
                self.getDate()
                self.reload()
                return
            case "отмена":
                return
            case "сохранить":
                return
            case _:
                raise Exception


class EditCategoryStep(Step):
    entity_types = ["text"]

    def reload(self):
        self.state.steps.append(
            EditCategoryStep(
                self.state,
                self.admin,
                message = StepMessages.text_edit_category_method,
                error_message = ErrorMessages.text,
                name = "method",
                reply_markup = edit_category_markup,
            )
        )

    def getTitle(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_edit_category_title,
                error_message = ErrorMessages.text,
                name = "title",
                reply_markup = None,
            )
        )

    def getPhoto(self):
        self.state.steps.append(
            GetPhoto(
                self.state,
                self.admin,
                message = StepMessages.text_edit_category_photo,
                error_message = ErrorMessages.photo,
                name = "photo",
                reply_markup = None,
            )
        )

    def parse_data(self, data, content_type = None):
        self.data = data

        match data.lower():
            case "название":
                self.getTitle()
                self.reload()
                return
            case "фото":
                self.getPhoto()
                self.reload()
                return
            case "отмена":
                return
            case "сохранить":
                return
            case _:
                raise Exception


class EditDishStep(Step):
    entity_types = ["text"]

    def reload(self):
        self.state.steps.append(
            EditDishStep(
                self.state,
                self.admin,
                message = StepMessages.text_edit_dish_method,
                error_message = ErrorMessages.text,
                name = "method",
                reply_markup = edit_dish_markup,
            )
        )

    def getTitle(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_title,
                error_message = ErrorMessages.text,
                name = "title",
                reply_markup = None,
            )
        )


    def getDescription(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_description,
                error_message = ErrorMessages.text,
                name = "description",
                reply_markup = None,
            )
        )


    def getPortion(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_portion,
                error_message = ErrorMessages.text,
                name = "portion",
                reply_markup = None,
            )
        )

    def getPrice(self):
        self.state.steps.append(
            GetNumber(
                self.state,
                self.admin,
                message = StepMessages.text_dish_price,
                error_message = ErrorMessages.number,
                name = "price",
                reply_markup = None,
            )
        )

    def parse_data(self, data, content_type = None):
        self.data = data

        match data.lower():
            case "название":
                self.getTitle()
                self.reload()
                return
            case "описание":
                self.getDescription()
                self.reload()
                return
            case "грамовка":
                self.getPortion()
                self.reload()
                return
            case "цена":
                self.getPrice()
                self.reload()
                return
            case "отмена":
                return
            case "сохранить":
                return
            case _:
                raise Exception


class OneMoreCreateDish(Step):
    entity_types = ["text"]

    def reload(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_title,
                error_message = ErrorMessages.text,
                name = "title",
                reply_markup = None,
            )
        )
        self.state.steps.append(
            OneMoreCreateDish(
                self.state,
                self.admin,
                message = StepMessages.text_create_dish_one_more,
                error_message = ErrorMessages.one_more,
                name = "one_more",
                reply_markup = yes_or_not_markup,
            )
        ) 

    def parse_data(self, data, content_type = None):
        self.data = data


        print(self.state.dump_data)

        match data.lower():
            case "да":
                self.admin.generateMethod(self.state.method_name, self.state.dump_data)
                self.reload()
                return
            case "нет":
                return
            case _:
                raise Exception
            

class OneMoreCreateDishSecond(Step):
    entity_types = ["text"]

    def reload(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_title,
                error_message = ErrorMessages.text,
                name = "title",
                reply_markup = None,
            )
        )
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_description,
                error_message = ErrorMessages.text,
                name = "description",
                reply_markup = None,
            )
        )
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_dish_portion,
                error_message = ErrorMessages.text,
                name = "portion",
                reply_markup = None,
            )
        )
        self.state.steps.append(
            GetNumber(
                self.state,
                self.admin,
                message = StepMessages.text_dish_price,
                error_message = ErrorMessages.number,
                name = "price",
                reply_markup = None,
            )
        )
        self.state.steps.append(
            OneMoreCreateDishSecond(
                self.state,
                self.admin,
                message = StepMessages.text_create_dish_one_more,
                error_message = ErrorMessages.one_more,
                name = "one_more",
                reply_markup = yes_or_not_markup,
            )
        ) 

    def parse_data(self, data, content_type = None):
        self.data = data


        print(self.state.dump_data)

        match data.lower():
            case "да":
                self.admin.generateMethod(self.state.method_name, self.state.dump_data)
                self.reload()
                return
            case "нет":
                return
            case _:
                raise Exception

class State:
    method_name = "pass"

    admin = None
    steps = []
    required_steps = []
    message = "Start state..."
    dump_data = {}

    def __init__(self, admin):
        print("self.required_steps")

        self.admin = admin
        self.admin.send_answer(self.message)
        self.dump_data = {}
        # self.admin.send_answer(self.message)
        self.steps = [
            step["method"](
                self,
                self.admin,
                message = step["message"],
                unique_message = step["unique_message"],
                error_message = step["error_message"],
                name = step["name"],
                reply_markup = step["reply_markup"],
            )
            for step
            in self.required_steps
        ]
        print(self.steps)
        self.activate()

    def activate(self):
        try:
            self.active_step().activate()
        except:
            self.admin.send_answer("No existed steps")

    def active_step(self):
        try:
            return self.steps[0]
        except:
            return None

    def next_step(self):
        self.dump_data[self.active_step().name] = self.active_step().data

        if len(self.steps) > 1:
            self.steps.pop(0)
            self.activate()
        else:
            self.finish()

    def next_step_append(self):
        try:
            self.dump_data[self.active_step().name].append(self.active_step().data)
        except:
            self.dump_data[self.active_step().name] = []
            self.dump_data[self.active_step().name].append(self.active_step().data)

        if len(self.steps) > 1:
            self.steps.pop(0)
            self.activate()
        else:
            self.finish()

    def exit(self):
        self.admin.send_answer("finish")
        self.admin.finish_state()

    def finish(self):
        # main_func(self.dump_data)
        # main_func = self.main_func
        self.admin.generateMethod(self.method_name, self.dump_data)
        self.admin.send_answer(f"Finish")
        # self.admin.send_answer(str(self.dump_data))
        self.dump_data = {}
        self.admin.finish_state()

class CreateState(State):
    pass

class CreateEvent(CreateState):
    method_name = "CreateEvent"
    message = StateMessages.create_event
    required_steps = [
        {
            "method": GetPhoto,
            "message": StepMessages.text_event_photo,
            "error_message": ErrorMessages.photo,
            "reply_markup": None,
            "name": "photo"
        },
        {
            "method": GetText,
            "message": StepMessages.text_event_title,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "title"
        },
        {
            "method": GetText,
            "message": StepMessages.text_event_description,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "description"
        },
        {
            "method": GetDate,
            "message": StepMessages.text_event_date,
            "error_message": ErrorMessages.date,
            "reply_markup": None,
            "name": "date"
        },
    ]

class CreateCategory(CreateState):
    method_name = "CreateCategory"
    message = StateMessages.create_category
    required_steps = [
        {
            "method": GetPhoto,
            "message": StepMessages.text_category_photo,
            "error_message": ErrorMessages.photo,
            "reply_markup": None,
            "name": "photo"
        },
        {
            "method": GetText,
            "message": StepMessages.text_category_title,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "title"
        },
    ]

class CreateDish(CreateState):
    method_name = "CreateDish"
    message = StateMessages.create_dish
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.text_create_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "category_id"
        },
        {
            "method": GetText,
            "message": StepMessages.text_dish_title,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "title"
        },
        # {
        #     "method": GetText,
        #     "message": StepMessages.text_dish_description,
        #     "error_message": ErrorMessages.text,
        #     "reply_markup": None,
        #     "name": "description"
        # },
        # {
        #     "method": GetText,
        #     "message": StepMessages.text_dish_portion,
        #     "error_message": ErrorMessages.text,
        #     "reply_markup": None,
        #     "name": "portion"
        # },
        # {
        #     "method": GetNumber,
        #     "message": StepMessages.text_dish_price,
        #     "error_message": ErrorMessages.number,
        #     "reply_markup": None,
        #     "name": "price"
        # },
        {
            "method": OneMoreCreateDish,
            "message": StepMessages.text_create_dish_one_more,
            "error_message": ErrorMessages.one_more,
            "reply_markup": yes_or_not_markup,
            "name": "one_more"
        },
    ]


class CreateDishSecond(CreateState):
    method_name = "CreateDishSecond"
    message = StateMessages.create_dish
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.text_create_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "frst_category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.text_create_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "category_id"
        },
        {
            "method": GetText,
            "message": StepMessages.text_dish_title,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "title"
        },
        {
            "method": GetText,
            "message": StepMessages.text_dish_description,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "description"
        },
        {
            "method": GetText,
            "message": StepMessages.text_dish_portion,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "portion"
        },
        {
            "method": GetNumber,
            "message": StepMessages.text_dish_price,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "price"
        },
        {
            "method": OneMoreCreateDishSecond,
            "message": StepMessages.text_create_dish_one_more,
            "error_message": ErrorMessages.one_more,
            "reply_markup": yes_or_not_markup,
            "name": "one_more"
        },
    ]

class EditState(State):
    pass

class EditEvent(EditState):
    method_name = "EditEvent"
    message = StateMessages.edit_event
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_event_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": EditEventStep,
            "message": StepMessages.text_edit_event_method,
            "error_message": ErrorMessages.text,
            "reply_markup": edit_event_markup,
            "name": "method",
        },
    ]

class EditCategory(EditState):
    method_name = "EditCategory"
    message = StateMessages.edit_category
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": EditCategoryStep,
            "message": StepMessages.text_edit_category_method,
            "error_message": ErrorMessages.text,
            "reply_markup": edit_category_markup,
            "name": "method",
        },
    ]

class EditDish(EditState):
    method_name = "EditDish"
    message = StateMessages.edit_dish
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_dish_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": EditDishStep,
            "message": StepMessages.text_edit_dish_method,
            "error_message": ErrorMessages.text,
            "reply_markup": edit_dish_markup,
            "name": "method"
        },
    ]

class EditDishSecond(EditState):
    method_name = "EditDishSecond"
    message = StateMessages.edit_dish
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "semi_category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.text_edit_dish_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": EditDishStep,
            "message": StepMessages.text_edit_dish_method,
            "error_message": ErrorMessages.text,
            "reply_markup": edit_dish_markup,
            "name": "method"
        },
    ]

class UploadPhotoStep(Step):
    entity_types = ["text", "photo"]

    def finish(self):
        self.state.next_step_append()

    def reload(self):
        self.state.steps.append(
            UploadPhotoStep(
                self.state,
                self.admin,
                message = "None",
                error_message = ErrorMessages.photo,
                name = "photos",
                reply_markup = None,
            )
        )

    # def getTitle(self):
    #     self.state.steps.append(
    #         GetText(
    #             self.state,
    #             self.admin,
    #             message = StepMessages.text_edit_category_title,
    #             error_message = ErrorMessages.text,
    #             name = "title",
    #             reply_markup = None,
    #         )
    #     )
    #
    # def getPhoto(self):
    #     self.state.steps.append(
    #         GetPhoto(
    #             self.state,
    #             self.admin,
    #             message = StepMessages.text_edit_category_photo,
    #             error_message = ErrorMessages.photo,
    #             name = "photo",
    #             reply_markup = None,
    #         )
    #     )

    def parse_data(self, data, content_type):
        self.data = data

        match content_type:
            case "text":
                match data.lower():
                    case "отмена":
                        return
                    case "сохранить":
                        return
                    case _:
                        raise Exception
            case "photo":
                # print(f"{content_type = }")
                # print(f"{data = }")
                self.data = io.BytesIO(data)
                # print(self.data())
                self.reload()
            case _:
                raise Exception

class CreatePhotoReport(CreateState):
    method_name = "CreatePhotoReport"
    message = StateMessages.create_photo_report
    required_steps = [
        {
            "method": GetText,
            "message": StepMessages.text_create_photo_report_title,
            "error_message": ErrorMessages.text,
            "reply_markup": None,
            "name": "title"
        },
        {
            "method": GetDate,
            "message": StepMessages.text_create_photo_report_date,
            "error_message": ErrorMessages.date,
            "reply_markup": None,
            "name": "date"
        },
        {
            "method": GetPhoto,
            "message": StepMessages.text_create_photo_report_photo,
            "error_message": ErrorMessages.photo,
            "reply_markup": None,
            "name": "photo"
        },
        {
            "method": UploadPhotoStep,
            "message": StepMessages.text_create_photo_report_photos,
            "error_message": ErrorMessages.photo,
            "reply_markup": photo_report_markup,
            "name": "photos"
        },
    ]

class EditPhotoReportStep(Step):
    entity_types = ["text"]

    def reload(self):
        self.state.steps.append(
            EditPhotoReportStep(
                self.state,
                self.admin,
                message = StepMessages.text_edit_category_method,
                error_message = ErrorMessages.text,
                name = "method",
                reply_markup = edit_photo_report_markup,
            )
        )


    def getTitle(self):
        self.state.steps.append(
            GetText(
                self.state,
                self.admin,
                message = StepMessages.text_create_photo_report_title,
                error_message = ErrorMessages.text,
                name = "title",
                reply_markup = None,
            )
        )
    def getDate(self):
        self.state.steps.append(
            GetDate(
                self.state,
                self.admin,
                message = StepMessages.text_create_photo_report_date,
                error_message = ErrorMessages.date,
                name = "date",
                reply_markup = None,
            )
        )
    def getPhoto(self):
        self.state.steps.append(
            GetPhoto(
                self.state,
                self.admin,
                message = StepMessages.text_create_photo_report_photo,
                error_message = ErrorMessages.photo,
                name = "photo",
                reply_markup = None,
            )
        )

    def parse_data(self, data, content_type = None):
        self.data = data

        match data.lower():
            case "название":
                self.getTitle()
                self.reload()
                return
            case "фото":
                self.getPhoto()
                self.reload()
                return
            case "дата":
                self.getDate()
                self.reload()
                return
            case "отмена":
                return
            case "сохранить":
                return
            case _:
                raise Exception

class EditPhotoReport(EditState):
    method_name = "EditPhotoReport"
    message = StateMessages.edit_photo_report
    required_steps = [
        {
            "method": GetNumber,
            # "message": StepMessages.text_edit_photo_report_id,
            "message": photoReportsIDsMessage(),
            "unique_message": photoReportsIDsMessage,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": EditPhotoReportStep,
            "message": StepMessages.text_edit_photo_report_method,
            "error_message": ErrorMessages.text,
            "reply_markup": edit_photo_report_markup,
            "name": "method"
        },
    ]

class DeleteOrNot(Step):
    entity_types = ["text"]

    def parse_data(self, data, content_type = None):
        self.data = data
        match data.lower():
            case "да":
                return
            case "нет":
                self.state.exit()
                return
            case _:
                raise Exception

class DeleteEvent(State):
    method_name = "DeleteEvent"
    message = StateMessages.delete_event
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.delete_event_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": DeleteOrNot,
            "message": StepMessages.realy_delete,
            "error_message": ErrorMessages.yes_or_not,
            "reply_markup": yes_or_not_markup,
            "name": "ok"
        },
    ]

class DeleteCategory(State):
    method_name = "DeleteCategory"
    message = StateMessages.delete_category
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.delete_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": DeleteOrNot,
            "message": StepMessages.realy_delete,
            "error_message": ErrorMessages.yes_or_not,
            "reply_markup": yes_or_not_markup,
            "name": "ok"
        },
    ]

class DeleteDish(State):
    method_name = "DeleteDish"
    message = StateMessages.delete_dish
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.delete_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.delete_dish_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": DeleteOrNot,
            "message": StepMessages.realy_delete,
            "error_message": ErrorMessages.yes_or_not,
            "reply_markup": yes_or_not_markup,
            "name": "ok"
        },
    ]

class DeleteDishSecond(State):
    method_name = "DeleteDishSecond"
    message = StateMessages.delete_dish
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.delete_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.delete_dish_category_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "semi_category_id"
        },
        {
            "method": GetNumber,
            "message": StepMessages.delete_dish_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": DeleteOrNot,
            "message": StepMessages.realy_delete,
            "error_message": ErrorMessages.yes_or_not,
            "reply_markup": yes_or_not_markup,
            "name": "ok"
        },
    ]

class DeletePhotoReport(State):
    method_name = "DeletePhotoReport"
    message = StateMessages.delete_photo_report
    required_steps = [
        {
            "method": GetNumber,
            "message": StepMessages.delete_photo_report_id,
            "error_message": ErrorMessages.number,
            "reply_markup": None,
            "name": "id"
        },
        {
            "method": DeleteOrNot,
            "message": StepMessages.realy_delete,
            "error_message": ErrorMessages.yes_or_not,
            "reply_markup": yes_or_not_markup,
            "name": "ok"
        },
    ]

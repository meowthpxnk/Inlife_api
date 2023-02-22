from app import bot, admin
from .reply_markups import *
from .message_templates import *
import requests
import io


def openPilImage(url):
    r = requests.get(url, stream=True)
    image = io.BytesIO(r.content)
    return image



# bot.send_message(-878940110, error_message)

def is_admin_has_active_state(func):
    def message_wrap(*args, **kwargs):
        if admin.state:
            admin.send_answer(exit_message)
        else:
            func(*args, **kwargs)
    return message_wrap


def admin_message_handler(func):
    def message_wrap(message):
        if (message.chat.id == admin.chat_id):
            func(message)
        else:
            bot.send_message(message.chat.id, error_message)
    return message_wrap

@bot.message_handler(commands=['help'])
@admin_message_handler
def help_command(message):
    admin.send_answer(help_message)

@bot.message_handler(commands=['start'])
@admin_message_handler
def start_command(message):
    bot.send_message(message.chat.id, 'ХЭЛП2', reply_markup = defaultMarkup)

@bot.message_handler(commands=['createEvent'])
@admin_message_handler
@is_admin_has_active_state
def create_event_command(message):
    admin.createEvent()

@bot.message_handler(commands=['createCategory'])
@admin_message_handler
@is_admin_has_active_state
def create_category_command(message):
    admin.createCategory()

@bot.message_handler(commands=['createDish'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.createDish()

@bot.message_handler(commands=['editEvent'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.editEvent()

@bot.message_handler(commands=['editDish'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.editDish()

@bot.message_handler(commands=['editCategory'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.editCategory()


@bot.message_handler(commands=['createPhotoReport'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.createPhotoReport()

@bot.message_handler(commands=['editPhotoReport'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.editPhotoReport()




@bot.message_handler(commands=['deleteEvent'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.deleteEvent()

@bot.message_handler(commands=['deleteCategory'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.deleteCategory()

@bot.message_handler(commands=['deleteDish'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.deleteDish()

@bot.message_handler(commands=['deletePhotoReport'])
@admin_message_handler
@is_admin_has_active_state
def create_dish_command(message):
    admin.deletePhotoReport()




@bot.message_handler(commands=['exit'])
@admin_message_handler
def exit_command(message):
    admin.state.exit()
    # bot.send_message(message.chat.id, 'ХЭЛП2', reply_markup = defaultMarkup)

@bot.message_handler(content_types=["text", "photo"])
@admin_message_handler
def get_message(message):
    # admin.send_answer(f"{admin}")
    
    # admin.state.next_step()
    # bot.send_message(message.chat.id, '<b>получил текст</b>', parse_mode = "HTML")

    try:
        mess = admin.state.method_name if admin.state else None
        admin.send_answer(f"{mess}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
        admin.send_answer(f"{id(admin)}")
    except Exception as e:
        admin.send_answer(f"{e}")

    try:


        if not admin.state:
            admin.send_answer(start_message)
            return

        content_type = message.content_type

        match content_type:
            case "text":
                admin.process_new_updates(message.text, content_type)
                return
            case "photo":
                fileID = message.photo[-1].file_id
                file = bot.get_file(fileID)
                image = bot.download_file(file.file_path)
                admin.process_new_updates(image, content_type)
                return
            case "document":
                return
            case _:
                return
    
    except Exception as e:
        admin.send_answer(f"{e}")
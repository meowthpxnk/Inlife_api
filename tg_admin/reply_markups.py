from telebot import types
from .buttons import *

default_markup = types.ReplyKeyboardMarkup(
    one_time_keyboard = True,
    resize_keyboard = True,
    selective = True,
    is_persistent = False,
)

defaultMarkup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
    ) \
    .add(button_title, button_photo, button_description, button_title)


edit_event_markup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
        row_width = 4
    ) \
    .add(button_event_photo, button_title, button_description, button_date) \
    .add(button_exit, button_save) \


# edit_event_markup = types.ReplyKeyboardMarkup(
#         one_time_keyboard = True,
#         resize_keyboard = True,
#         selective = True,
#         is_persistent = False,
#         row_width = 4
#     ) \
#     .add(button_photo, button_title) \
#     .add(button_exit, button_save) \

edit_category_markup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
        row_width = 2
    ) \
    .add(button_title, button_photo) \
    .add(button_exit, button_save) \

edit_dish_markup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
        row_width = 4
    ) \
    .add(button_title, button_description, button_portion, button_price) \
    .add(button_exit, button_save) \

yes_or_not_markup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
        row_width = 2
    ) \
    .add(button_yes, button_no)


photo_report_markup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
        row_width = 2
    ) \
    .add(button_exit, button_save)

edit_photo_report_markup = types.ReplyKeyboardMarkup(
        one_time_keyboard = True,
        resize_keyboard = True,
        selective = True,
        is_persistent = False,
        row_width = 3
    ) \
    .add(button_title, button_date, button_photo) \
    .add(button_exit, button_save)

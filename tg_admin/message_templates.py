from test import getPhotoReportsItems, getEventItems, getDishesItems, getCategoriesItems, getSemiCategoriesItems

def photoReportsIDsMessage(arg = None):
    return "".join([f"{item.id}. {item.title}\n" for item in getPhotoReportsItems(arg)])

def eventsIDsMessage(arg = None):
    return "".join([f"{item.id}. {item.title}\n" for item in getEventItems(arg)])

def dishesIDsMessage(arg = None):
    return "".join([f"{item.id}. {item.title}\n" for item in getDishesItems(arg)])

def categoriesIDsMessage(arg = None):
    return "".join([f"{item.id}. {item.title}\n" for item in getCategoriesItems(arg)])

def semiCategoriesIDsMessage(arg = None):
    return "".join([f"{item.id}. {item.title}\n" for item in getSemiCategoriesItems(arg)])

help_message = "<b>Доступные команды: </b>\n\n\
\
<b>Мероприятия:</b>\n\
<b>/createEvent</b> - создание\n\
<b>/editEvent</b> - редактирование\n\
<b>/deleteEvent</b> - удаление\n\n\
\
<b>Фото-отчеты:</b>\n\
<b>/createPhotoReport</b> - создание\n\
<b>/editPhotoReport</b> - редактирование\n\
<b>/deletePhotoReport</b> - удаление\n\n\
\
<b>Меню:</b>\n\
<b>Категории Блюд</b>\n\
<b>/createCategory</b> - создание\n\
<b>/editCategory</b> - редактирование\n\
<b>/deleteCategory</b> - удаление\n\n\
\
<b>Подкатегории блюд</b>\n\
<b>/createSemiCategory</b> - создание\n\
<b>/editSemiCategory</b> - редактирование\n\
<b>/deleteSemiCategory</b> - удаление\n\n\
\
<b>Блюда</b>\n\
<b>/createDish</b> - создание\n\
<b>/editDish</b> - редактирование\n\
<b>/deleteDish</b> - удаление\n\n\
"

manual_message = "\
<b>Мануал по использованию!</b>\n\n\
<b>Мероприятия:</b>\n\
Для того чтобы создать мероприятие используйте команду /createEvent, скиньте фото будущего мероприятия, введите название, введите дату в формате DD/MM/YYYY(HH:MM)*, \
например '13/02/2023(22:30). Для изменения информации мероприятия воспользуйтесь командой /editEvent, выберите ID мероприятия из преложенных, выберете кнопку на клавиатуре а затем внесите информацию. по завершению редактирования нажмите кнопку сохранить, или отменить.'\
Для удаления мероприятия используйте команду /deleteEvent, выберите ID мероприятия и нажмите 'Да'\n\n\
<b>Фотоотчеты:</b>\n\
Для создания фотоотчета - /createPhotoReport, введите название и скинте обложку, введите дату в формате DD/MM/YY(HH:MM)*, время можно ставить любое, можно писать так '13/02/2023(00:00)' время ставить 00:00 (но не обязательноб тк нет разницы), после этого загрузите фотографии которые хотите отобразить, по завершении загрузки фото выберите кнопку сохранить\
Для удаления - /deletePhotoReport выберите ID и удалить\
Для редактирования - /editPhotoReport\n\n\
<b>Меню:</b>\n\
Сперва создайте категорию - /createCategory, затем под-категорию - /createSemiCategory, выберите ID ранее созданной категории (можно создать сразу несколько для одной и той же категории), затем /createDish выберите ID категории и подкатегории и заполните информацию нового блюда (Можно созать несколько для одной подкатегории)\
Редактирование (/editCatgeory, /editSemiCategory, /editDish)\
Удаление (/deleteCategory, /deleteSemiCategory, /deleteDish)\n\n\
* DD/MM/YYYY(HH:MM) - формат даты, где DD - дни, MM - Месяц, YYYY - год, HH - часы и MM - минуты\
"

error_message = "У вас нет прав на использование этого бота"

exit_message = "Введите /exit"

start_message = "<b>Запустите редактирование сайта.</b>\n\n/help - Для помощи"

class ErrorMessages:
    photo = "Неверный формат фотографии"
    text = "Неверный формат сообщения"
    date = "Неверный формат даты"
    number = "Неверный формат числа"

    one_more = "Введите да или нет"

    yes_or_not = "Введите да или нет"


class StepMessages:
    photo = "Отправьте фото"
    text = "Введите текст"
    date = "Введите дату в формате: DD/MM/YYYY(HH:MM)"

    text_category_photo = "Отправьте фото для категории"
    text_category_title = "Введите название категории"

    text_event_title = "Введите название мероприятия"
    text_event_date = "Введите дату мероприятия в формате: DD/MM/YYYY(HH:MM)"
    text_event_description = "Введите описание мероприятия"
    text_event_photo = "Отправьте афишу мероприятия"

    text_dish_title = "Введите название блюда"
    text_dish_description = "Введите описание/ингредиенты блюда"
    text_dish_portion = "Введите грамовку/порцию блюда"
    text_dish_price = "Введите цену блюда"

    text_edit_event_id = "Введите номер мероприятия для редактирования"
    text_edit_event_method = "Выберете метод"
    text_edit_event_title = "Введите название"
    text_edit_event_date = "Введите дату"
    text_edit_event_description = "Введите описание"
    text_edit_event_photo = "Отправьте фото"

    text_edit_category_id = "Введите id категории"
    text_edit_category_method = "Выберете метод"
    text_edit_category_title = "Введите название"
    text_edit_category_photo = "Отправьте фото"

    text_create_dish_category_id = "Выберете id категории для которой добавить блюдо"
    text_create_dish_one_more = "Создать еще одно блюдо для этой категории"


    text_edit_dish_category_id = "Выберете id категории редактируемого блюда"
    text_edit_dish_id = "Выберете id блюда"
    text_edit_dish_method = "Выберете метод"

    text_create_photo_report_title = "Введите название"
    text_create_photo_report_date = "Введите дату"
    text_create_photo_report_photo = "Отправьте обложку фото-отчета"
    text_create_photo_report_photos = "Отправьте фотографии"

    text_edit_photo_report_id = "Введите id фото-отчета"
    text_edit_photo_report_method = "Выберете метод"

    delete_event_id = "Введите id мероприятия для удаления"
    delete_dish_id = "Введите id блюда для удаления"
    delete_dish_category_id = "Введите id категории"
    delete_category_id = "Введите id категории для удаления"
    delete_photo_report_id = "Введите id фотоотчета для удаления"
    realy_delete = "Действительно удалить?"


class StateMessages:
    create_event = "<b>Создание мероприятия</b>"
    edit_event = "<b>Редактирование мероприятия</b>"
    delete_event = "<b>Удаление мероприятия</b>"

    create_category = "<b>Создание категории</b>"
    edit_category = "<b>Редактирование категории</b>"
    delete_category = "<b>Удаление категории</b>"

    create_dish = "<b>Создание блюда</b>"
    edit_dish = "<b>Редактирование блюда</b>"
    delete_dish = "<b>Удаление блюда</b>"

    create_photo_report = "<b>Создание фотоотчета</b>"
    edit_photo_report = "<b>Редактирование фотоотчета</b>"
    delete_photo_report = "<b>Удаление фотоотчета</b>"

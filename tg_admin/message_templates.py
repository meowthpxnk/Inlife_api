def photoReportsIDsMessage():
    return "asdiasd"

help_message = "<b>Доступные команды: </b>\n\n\
\
<b>Мероприятия</b>\n\
<b>/createEvent</b> - создание\n\
<b>/editEvent</b> - редактирование\n\
<b>/deleteEvent</b> - удаление\n\n\
\
<b>Категории Блюд</b>\n\
<b>/createCategory</b> - создание\n\
<b>/editCategory</b> - редактирование\n\
<b>/deleteCategory</b> - удаление\n\n\
\
<b>Блюда</b>\n\
<b>/createDish</b> - создание\n\
<b>/editDish</b> - редактирование\n\
<b>/deleteDish</b> - удаление\n\n\
\
<b>Фото-отчеты</b>\n\
<b>/createPhotoReport</b> - создание\n\
<b>/editPhotoReport</b> - редактирование\n\
<b>/deletePhotoReport</b> - удаление"

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

main_menu='''\n Главное меню:
    1.Открыть файл.
    2. Сохранить файл.
    3. Показать контакт.
    4. Добавить контакт.
    5. Найти контакт.
    6. Изменить контакт.
    7. Удалить контакт.
    8. Выход. \n'''
input_choice='Выберите пункт меню: '
load_successful='Телефонная книга успешно открыта'
pb_empty='Телефонная книга пуста или не загружена'
input_new_contact='Введите данные нового контакта: '
new_contact={'name':'Введите имя: ','phone':'Введите номер телефона: ','comment':'Введите комментарий: '}
def new_contact_successful(name:str):
    return f'Контакт {name} успешно добавлен'
def main_menu():
    print('\n1. Показать телефонную книгу.')
    print('2. Открыть файл телефонной книги.')
    print('3. Сохранить файл телефонной книги')
    print('4. Добавить контакт.')
    print('5. Изменить контакт.')
    print('6. Удалить контакт.')
    print('7. Найти контакт.')
    print('0. Выход.\n')
    return choice_main_menu()


def choice_main_menu():
    while True:
        try:
            choice = int(input('Выберите пункт меню от 0 до 7: '))
            if choice in range(0, 8):
                return choice
            else:
                print('Такого пункта нет, повторите попытку.')
        except:
            print('Не корректный ввод, выберите пункт из меню.')


def print_phone_book(phone_book: list):
    if len(phone_book) > 0:
        for id, contacts in enumerate(phone_book, 1):
            print(id, *contacts)
    else:
        print('Телефонная книга пуста или не загружена.')


def log_off():
    print('Все-го хоро-шего!')


def load_book():
    print('Телефонная книга успешно загружена.')


def save_book():
    print('Телефонная книга успешно сохранена.')


def remove_contact():
    print('Контакт успешно удален.')


def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите номер контакта: ')
    note = input('Введите заметку к контакту: ')
    return [name, phone, note]


def input_remove_contact():
    id = int(input('Введите ID контакта, который надо удалить: '))
    return id


def print_find_contact(phone_book: list):
    if len(phone_book) > 0:
        print('\nТелефонная книга на данный момент имеет вид: ')
        for id, contact in enumerate(phone_book, 1):
            print(id, *contact)
    else:
        print('\nПо указанным параметрам ни один контакт не найден. Уточните параметры поиска.')


def find_input():
    text = input('\nПо какому параметру выполнить поиск контактов?\n'
                 'Введите полностью или частично ФИО / номер / комментарий:\n'
                 '>>> ')
    return text


def find_error():
    print('\nПо указанным параметрам ни один контакт не найден. Уточните параметры поиска.')


def remove_choice():
    try:
        id = int(input('\nВведите ID номер контакта для удаления: '))
        return id
    except:
        print('\nВведены некорректные данные! Укажите ID контакта.')


def remove_error():
    print('\nУдаление контакта не выполнено! Проверьте корректность введения ID.')


def save_error():
    print('\nСохранение телефонной книги не выполнено! Книга пуста.')


def change_choice():
    try:
        id = int(input('\nВведите ID номер контакта для изменения: '))
        return id
    except:
        print('\nВведены некорректные данные! Укажите ID контакта.')


def change_successful():
    print('\nИзменение контакта выполнено успешно.')


def change_error():
    print('\nИзменение контакта не выполнено! Проверьте корректность введения ID.')



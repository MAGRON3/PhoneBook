"""
1 Создать файл ++
1.1 Открыть файл на дозапись +
2 Запись контакта в файл ++
2.1 Открыть файл на дозапись +
2.2 Получить данные нового контакта +
2.3 Записать эти данные в файл +
3 Вывод данных на экран ++
3.1 Открыть файл на чтение +
3.2 Получить данные из файла +
3.3 Вывести данные на экран +
4 Поиск контакта по данным ++
4.1 Получить данные для поиска +
4.2 Выбрать варианта поиска +
4.3 Открыть файл на чтение +
4.4 Получить данные из файла +
4.5 Осуществить поиск +
4.6 Вывести на экран +
5 Создать UI ++
5.1 Вывод на экран пользовательского меню +
5.2 Получить запрос от пользователя +
5.3 Запуск соответсвующей функции +
5.4 Выход из программы +
"""


def input_name():
    return input("Введите имя: ")


def input_surname():
    return input("Введите фамилию: ")


def input_patronumic():
    return input("Введите отчество: ")


def input_phone():
    return input("Введите номер телефона: ")


def input_address():
    return input("Введите адрес: ")


def create_contact():
    print("Введите данные контакта...")
    name = input_name()
    surname = input_surname()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f"{name} {surname} {patronumic} {phone}\n{address}\n\n"


def add_contact(contact, phonebook_num=0):
    print("Добавление контакта...")
    if not contact:
        contact = create_contact()
    else:
        contact += "\n\n"
    if phonebook_num == 0:
        phonebook_name = "phonebook.txt"
    else:
        phonebook_name = "phonebook_2.txt"
    with open(phonebook_name, "a", encoding="UTF-8") as f_w:
        f_w.write(contact)


def print_phonebook(phonebook_num=0):
    print("\n")
    if phonebook_num == 0:
        phonebook_name = "phonebook.txt"
    else:
        phonebook_name = "phonebook_2.txt"
    with open(phonebook_name, "r", encoding="UTF-8") as f_r:
        contacts_str = f_r.read()
        list_contacts = contacts_str.rstrip().split("\n\n")
        line_itr = 1
        for contact in list_contacts:
            print(f'{line_itr}: {contact}')
            line_itr += 1
    print("\n")


def find_contact(phonebook_num=0):
    search = input("Введите данные для поиска: ")
    print(
        "Возможные варианты поиска:\n"
        "1. По имени\n"
        "2. По фамилии\n"
        "3. По отчеству\n"
        "4. По телефону\n"
        "5. По адресу\n"
    )
    var = input("Выберите вариант поиска: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод!")
        var = input("Выберите вариант поиска: ")
    i_var = int(var) - 1
    if phonebook_num == 0:
        phonebook_name = "phonebook.txt"
    else:
        phonebook_name = "phonebook_2.txt"
    with open(phonebook_num, "r", encoding="UTF-8") as f_r:
        contacts_str = f_r.read()
        list_contacts = contacts_str.rstrip().split("\n\n")
        for contact in list_contacts:
            contact_lst = contact.split()
            if search in contact_lst[i_var]:
                print(contact)


def copy_contact():
    with open("phonebook.txt", "r", encoding="UTF-8") as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    with open("phonebook_2.txt", "r", encoding="UTF-8") as f2_r:
        contacts_str_2 = f2_r.read()
    list_contacts_2 = contacts_str_2.rstrip().split("\n\n")
    line_itr = 0
    for contact in list_contacts:
        print(f'{line_itr}: {contact}')
        line_itr += 1
    var = input("Введите номер контакта для копирования: ")
    i_var = int(var) - 1
    while i_var > len(list_contacts):
        print("Номер некорректен")
        var = input("Введите номер контакта для копирования: ")
        i_var = int(var) - 1
    line_to_copy = list_contacts[i_var]
    if line_to_copy in list_contacts_2:
        print("Контакт существует в справочнике")
    else:
        add_contact(line_to_copy, 1)


def ui():
    with open("phonebook.txt", "a", encoding="UTF-8"):
        pass
    with open("phonebook_2.txt", "a", encoding="UTF-8"):
        pass
    choise = "0"
    while choise != "5":
        print(
            "\n\tВозможные варианты действий:\n"
            "1. Добавление нового контакта\n"
            "2. Вывод данных на экран\n"
            "3. Поиск контакта\n"
            "4. Копирование контакта\n"
            "5. Выход из программы\n"
        )
        choise = input("Выберите вариант действия: ")
        while choise not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод!")
            choise = input("Выберите вариант действия: ")

        if choise == "1":
            add_contact(None)
        elif choise == "2":
            print_phonebook()
        elif choise == "3":
            find_contact()
        elif choise == "4":
            copy_contact()
        else:
            print("Всего доброго!")


ui()

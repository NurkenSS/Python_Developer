from personal.personal_info import input_personal_info, output_personal_info
from business.business_info import input_business_info, output_business_info


def main_menu():
    """Главное меню программы."""
    while True:
        print("\nГлавное меню:")
        print("1 — Ввести или обновить информацию")
        print("2 — Вывести информацию")
        print("0 — Завершить работу")
        
        choice = input("Введите номер пункта меню: ")
        if choice == "1":
            input_menu()
        elif choice == "2":
            output_menu()
        elif choice == "0":
            print("Завершение работы.")
            break
        else:
            print("Некорректный пункт меню. Повторите ввод.")


def input_menu():
    """Меню ввода информации."""
    while True:
        print("\nМеню ввода информации:")
        print("1 — Личная информация")
        print("2 — Информация о предпринимателе")
        print("0 — Назад")
        
        choice = input("Введите номер пункта меню: ")
        if choice == "1":
            input_personal_info()
        elif choice == "2":
            input_business_info()
        elif choice == "0":
            break
        else:
            print("Некорректный пункт меню. Повторите ввод.")


def output_menu():
    """Меню вывода информации."""
    while True:
        print("\nМеню вывода информации:")
        print("1 — Личная информация")
        print("2 — Вся информация")
        print("0 — Назад")
        
        choice = input("Введите номер пункта меню: ")
        if choice == "1":
            output_personal_info()
        elif choice == "2":
            output_personal_info()
            output_business_info()
        elif choice == "0":
            break
        else:
            print("Некорректный пункт меню. Повторите ввод.")

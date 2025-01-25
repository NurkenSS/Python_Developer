personal_info = {
    "name": "",
    "age": 0,
    "phone": "",
    "email": "",
    "postal_index": "",
    "postal_address": "",
    "additional_info": ""
}

def input_personal_info():
    """Ввод личной информации пользователя."""
    print("Введите личную информацию:")
    personal_info["name"] = input("Имя: ")
    while True:
        try:
            age = int(input("Возраст: "))
            if age < 0:
                raise ValueError
            personal_info["age"] = age
            break
        except ValueError:
            print("Ошибка: возраст должен быть неотрицательным числом.")
    personal_info["phone"] = input("Телефон: ")
    personal_info["email"] = input("Электронная почта: ")
    postal_index = input("Индекс: ")
    personal_info["postal_index"] = ''.join(filter(str.isdigit, postal_index))
    personal_info["postal_address"] = input("Почтовый адрес: ")
    personal_info["additional_info"] = input("Дополнительная информация: ")

def output_personal_info():
    """Вывод личной информации."""
    print("\nЛичная информация:")
    for key, value in personal_info.items():
        print(f"{key.capitalize()}: {value}")
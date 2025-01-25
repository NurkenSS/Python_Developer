business_info = {
    "ogrnip": "",
    "inn": "",
    "bank_account": "",
    "bank_name": "",
    "bik": "",
    "correspondent_account": ""
}

def input_business_info():
    """Ввод информации о предпринимателе."""
    print("Введите информацию о предпринимателе:")
    while True:
        ogrnip = input("ОГРНИП (15 цифр): ")
        if len(ogrnip) == 15 and ogrnip.isdigit():
            business_info["ogrnip"] = ogrnip
            break
        else:
            print("Ошибка: ОГРНИП должен содержать ровно 15 цифр.")
    while True:
        inn = input("ИНН: ")
        if inn.isdigit():
            business_info["inn"] = inn
            break
        else:
            print("Ошибка: ИНН должен быть числом.")
    while True:
        bank_account = input("Расчётный счёт (20 цифр): ")
        if len(bank_account) == 20 and bank_account.isdigit():
            business_info["bank_account"] = bank_account
            break
        else:
            print("Ошибка: расчётный счёт должен содержать ровно 20 цифр.")
    business_info["bank_name"] = input("Название банка: ")
    while True:
        bik = input("БИК: ")
        if bik.isdigit():
            business_info["bik"] = bik
            break
        else:
            print("Ошибка: БИК должен быть числом.")
    while True:
        correspondent_account = input("Корреспондентский счёт: ")
        if correspondent_account.isdigit():
            business_info["correspondent_account"] = correspondent_account
            break
        else:
            print("Ошибка: корреспондентский счёт должен быть числом.")

def output_business_info():
    """Вывод информации о предпринимателе."""
    print("\nИнформация о предпринимателе:")
    for key, value in business_info.items():
        print(f"{key.capitalize()}: {value}")

while True:
    number = input("Введите число: ")

    if number == "exit":
        print("Выход из программы...")
        break

    if number.lstrip("-").isdigit():
        print(f"В этом числе {len(number.lstrip('-'))} цифры.")
    else:
        print("Ошибка: данные не являются числом.")

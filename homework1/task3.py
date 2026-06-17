age = input("Введите ваш возраст: ")

if age.lstrip("-").isdigit():
    age = int(age)

    if age < 0:
        print("Ошибка: возраст не может быть отрицательным!")
    elif age >= 18:
        print("Вы совершеннолетний.")
    else:
        print("Вы несовершеннолетний.")
else:
    print("Ошибка: введено не число!")

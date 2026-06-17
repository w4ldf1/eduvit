name = input("Ваше имя: ")
surname = input("Фамилия: ")
age = input("Возраст: ")

result_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет.".format(name, surname, age)
result_f_string = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."

print()
print("Реализация через format:")
print(result_format)
print()
print("Реализация через f-string:")
print(result_f_string)

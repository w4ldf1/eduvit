def factorial(number):
    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


squares = [number ** 2 for number in range(1, 11)]
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
days_numbers = {day: index for index, day in enumerate(days, start=1)}
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
lower_tags = {tag.lower() for tag in tags}
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [number for number in numbers if number % 2 == 0]
factorials = {number: factorial(number) for number in range(1, 6)}

print("1.", squares)
print("2.", days_numbers)
print("3.", lower_tags)
print("4.", even_numbers)
print("5.", factorials)

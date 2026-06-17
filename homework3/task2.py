from typing import Union


Number = Union[int, float]


def check_number(value: Number) -> None:
    if not isinstance(value, (int, float)):
        raise TypeError("Аргумент должен быть числом")


def addition(first: Number, second: Number) -> Number:
    check_number(first)
    check_number(second)
    return first + second


def subtraction(first: Number, second: Number) -> Number:
    check_number(first)
    check_number(second)
    return first - second


def multiplication(first: Number, second: Number) -> Number:
    check_number(first)
    check_number(second)
    return first * second


def division(first: Number, second: Number) -> float:
    check_number(first)
    check_number(second)

    if second == 0:
        raise ZeroDivisionError("делитель не может быть нулем")

    return first / second


def power(first: Number, second: Number) -> Number:
    check_number(first)
    check_number(second)

    if first == 0 and second < 0:
        raise ValueError("ноль нельзя возводить в отрицательную степень")

    return first ** second


def factorial(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError("Аргумент должен быть целым числом")

    if number < 0:
        raise ValueError("факториал отрицательного числа не определен")

    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def sinus(number: Number) -> float:
    check_number(number)
    result = 0

    for index in range(10):
        sign = -1 if index % 2 else 1
        result += sign * number ** (2 * index + 1) / factorial(2 * index + 1)

    return result


def median(numbers: list[Number]) -> Number:
    if not isinstance(numbers, list):
        raise TypeError("Аргумент должен быть списком")

    if len(numbers) == 0:
        raise ValueError("список не должен быть пустым")

    for number in numbers:
        check_number(number)

    sorted_numbers = sorted(numbers)
    middle = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[middle]

    return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2


def print_operations() -> None:
    print("Доступные операции:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Возведение в степень")
    print("6. Факториал")
    print("7. Синус")
    print("8. Медиана")
    print("--------------------")


while True:
    print_operations()
    operation = input("Операция: ")

    if operation == "exit":
        break

    try:
        operation = int(operation)

        if operation == 1:
            first = float(input("Слагаемое 1: "))
            second = float(input("Слагаемое 2: "))
            print(">>>", addition(first, second))
        elif operation == 2:
            first = float(input("Уменьшаемое: "))
            second = float(input("Вычитаемое: "))
            print(">>>", subtraction(first, second))
        elif operation == 3:
            first = float(input("Множитель 1: "))
            second = float(input("Множитель 2: "))
            print(">>>", multiplication(first, second))
        elif operation == 4:
            first = float(input("Делимое: "))
            second = float(input("Делитель: "))
            print(">>>", division(first, second))
        elif operation == 5:
            first = float(input("Число: "))
            second = float(input("Степень: "))
            print(">>>", power(first, second))
        elif operation == 6:
            number = int(input("Число: "))
            print(">>>", factorial(number))
        elif operation == 7:
            number = float(input("Число: "))
            print(">>>", round(sinus(number), 6))
        elif operation == 8:
            numbers = list(map(float, input("Список чисел: ").split()))
            print(">>>", median(numbers))
        else:
            print("Ошибка: неизвестная операция")
    except ValueError as error:
        print("Ошибка значения:", error)
    except TypeError as error:
        print("Ошибка типа:", error)
    except ZeroDivisionError as error:
        print("Математическая ошибка:", error)

    print("--------------------")

def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except ValueError:
                return "Bad request"

    return round(sum(list_num) / len(list_num), 2)


assert average_num([1, 1]) == 1
assert average_num([2.5, 3.5]) == 3
assert average_num([1, 2, 3, 4]) == 2.5
assert average_num(["1", "2", "3"]) == 2
assert average_num([10, "20", 30]) == 20
assert average_num([-10, 10]) == 0
assert average_num([1.111, 2.222, 3.333]) == 2.22
assert average_num(["10", "hello"]) == "Bad request"
assert average_num([0, 0, 0]) == 0
assert average_num([100]) == 100

print("Все assert-тесты для average_num пройдены")

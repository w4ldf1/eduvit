def multiply_items(items: list[int], multiplier: int = 2) -> list[int]:
    return [item * multiplier for item in items]


multiply_items_lambda = lambda items, multiplier=2: list(map(lambda item: item * multiplier, items))

numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
multiplier_input = input("Введите множитель (по умолчанию 2): ")

if multiplier_input:
    multiplier = int(multiplier_input)
else:
    multiplier = 2

print("Результат (функция):", multiply_items(numbers, multiplier))
print("Результат (лямбда-функция):", multiply_items_lambda(numbers, multiplier))

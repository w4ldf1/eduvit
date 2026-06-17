first_list = list(map(int, input("Введите первый список: ").split()))
second_list = list(map(int, input("Введите второй список: ").split()))

second_set = set(second_list)
common_elements = []

for number in first_list:
    if number in second_set and number not in common_elements:
        common_elements.append(number)

print("Общие элементы:", " ".join(map(str, common_elements)))

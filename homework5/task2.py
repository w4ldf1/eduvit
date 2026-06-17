import math
import random
import statistics


numbers = [random.randint(1, 100) for _ in range(100)]

average = round(statistics.mean(numbers), 2)
median = statistics.median(numbers)
deviation = round(statistics.stdev(numbers), 2)
sum_root = round(math.sqrt(sum(numbers)), 2)

print(f"Среднее: {average}, Медиана: {median}, Стандартное отклонение: {deviation}, Корень из суммы: {sum_root}")

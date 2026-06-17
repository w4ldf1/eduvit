import random
from array import array
from datetime import datetime, timedelta


today = datetime.today().date()
days_count = 365 * 5
random_days = array("I", [random.randint(0, days_count) for _ in range(10)])
dates = [today - timedelta(days=days) for days in random_days]

for index in range(len(dates) - 1):
    first_date = dates[index]
    second_date = dates[index + 1]
    difference = abs((first_date - second_date).days)
    print(f"Разница между {first_date} и {second_date}: {difference} дней")

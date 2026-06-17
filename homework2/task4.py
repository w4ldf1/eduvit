words = input("Введите строку: ").lower().split()
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 0

    counts[word] += 1

for word, count in counts.items():
    print(f"{word}: {count}")

def append_to_file(text, filename):
    file_path = f"{__file__.rsplit('/', 1)[0]}/{filename}"

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(text + "\n")

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for index, line in enumerate(lines, start=1):
        if index % 2 == 0:
            print(line.strip())


append_to_file("Пятая строка", "example.txt")

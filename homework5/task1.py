import random
from pathlib import Path


def create_file_name(length):
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    name = ""

    for _ in range(length):
        name += random.choice(symbols)

    return f"{name}.txt"


def create_random_files(directory_name, files_count=10, name_length=8):
    directory = Path(__file__).parent / directory_name
    directory.mkdir(exist_ok=True)
    created_files = []
    used_names = set()

    for old_file in directory.glob("*.txt"):
        old_file.unlink()

    while len(created_files) < files_count:
        file_name = create_file_name(name_length)

        if file_name in used_names:
            continue

        used_names.add(file_name)
        file_path = directory / file_name
        file_path.write_text("", encoding="utf-8")
        created_files.append(file_path)

    return created_files


files = create_random_files("random_files")

for file in files:
    print(file.resolve())

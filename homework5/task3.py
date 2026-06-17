import json
import random
import string


def create_password(length):
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(symbols)

    return password


names = ["John Doe", "Alex Smith", "Ivan Petrov", "Maria Green", "Anna Brown"]
name = random.choice(names)
email_name = name.lower().replace(" ", ".")

user = {
    "name": name,
    "age": random.randint(18, 70),
    "email": f"{email_name}@example.com",
    "password": create_password(12),
}

file_path = f"{__file__.rsplit('/', 1)[0]}/user.json"

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(user, file, indent=4)

with open(file_path, "r", encoding="utf-8") as file:
    saved_user = json.load(file)

print(json.dumps(saved_user, indent=4))

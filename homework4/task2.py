def is_prime(number):
    if number < 2:
        return False

    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            return False

    return True


def prime_numbers():
    number = 2

    while True:
        if is_prime(number):
            yield number

        number += 1


generator = prime_numbers()

for _ in range(10):
    print(next(generator))

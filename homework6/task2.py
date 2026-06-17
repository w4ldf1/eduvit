def is_palindrome(text):
    normalized = ""

    for symbol in text.lower():
        if symbol.isalnum():
            normalized += symbol

    return normalized == normalized[::-1]


assert is_palindrome("Лёша на полке клопа нашёл") is True
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("12321") is True
assert is_palindrome("hello") is False
assert is_palindrome("Топот") is True
assert is_palindrome("Я иду с мечем судия") is True
assert is_palindrome("Python") is False

print("Все assert-тесты для is_palindrome пройдены")

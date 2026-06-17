from typing import Union


def function_name(search: str, status: bool, *args: Union[int, str], **kwargs: Union[int, str]) -> Union[list[int], str]:
    """
    Обрабатывает позиционные или именованные аргументы.

    search выбирает режим работы: args или kwargs.
    status определяет, нужно ли вернуть только целые числа из args.
    args содержит произвольные позиционные значения.
    kwargs содержит произвольные именованные значения.
    Возвращает список чисел или строку с объединенными значениями.
    """
    result: list[int] = []
    result_text: str = ""

    if search == "args":
        if status:
            for item in args:
                if isinstance(item, int):
                    result.append(item)

            return result

        for item in args:
            result_text += f"{item}"

        return result_text

    if search == "kwargs":
        for key, value in kwargs.items():
            result_text += "Key: {}, Value: {}; ".format(key, value)

        return result_text

    raise ValueError("Error for search")


print(function_name("args", True, 1, "hello", 4, "test", 8))
print(function_name("args", False, 1, "hello", 4, "test", 8))
print(function_name("kwargs", True, name="Ivan", age=20))

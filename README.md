# eduvit

Учебный репозиторий для заданий по JavaScript, Python, React и Django.

## Структура

- `conversion` - перевод тернарных выражений в `if...else` и `switch`.
- `calculator` - примитивный калькулятор на HTML и JavaScript.
- `homework1` - первое домашнее задание по Python.
- `homework2` - задание по структурам данных Python.
- `homework3` - задание по функциям, типизации и классам Python.
- `homework4` - задание по генераторам, файлам и декораторам Python.
- `homework5` - задание по библиотекам и импортам Python.
- `homework6` - задание по тестированию Python.
- `graphic.py` - построение графика функции через `numpy` и `matplotlib`.
- `users` - React-приложение для сопоставления пользователей и постов.
- `Django` - сайт организации с новостями, комментариями и авторизацией.

## Проверка JavaScript

```bash
node conversion/Tern1.js
node conversion/Tern2.js
```

Калькулятор можно открыть в браузере через файл:

```text
calculator/h.html
```

## Проверка Python homework1

```bash
python3 homework1/task1.py
python3 homework1/task2.py
python3 homework1/task3.py
python3 homework1/task4.py
```

## Проверка Python homework2

```bash
python3 homework2/task1.py
python3 homework2/task2.py
python3 homework2/task3.py
python3 homework2/task4.py
```

## Проверка Python homework3

```bash
python3 homework3/task1.py
python3 homework3/task2.py
python3 homework3/task3.py
python3 homework3/task4.py
```

## Проверка Python homework4

```bash
python3 homework4/task1.py
python3 homework4/task2.py
python3 homework4/task3.py
python3 homework4/task4.py
```

## Проверка Python homework5

```bash
python3 homework5/task1.py
python3 homework5/task2.py
python3 homework5/task3.py
python3 homework5/task4.py
```

## Проверка Python homework6

```bash
python3 homework6/task1.py
python3 homework6/task2.py
python3 homework6/task3.py
```

## Проверка графика

```bash
python3.11 -m venv .venv
.venv/bin/pip install numpy matplotlib
.venv/bin/python graphic.py
```

## Проверка React users

```bash
cd users
npm install
npm run dev
```

## Проверка Django

```bash
cd Django
../.venv/bin/pip install -r requirements.txt
../.venv/bin/python manage.py migrate
../.venv/bin/python manage.py seed_demo
../.venv/bin/python manage.py runserver
```

После `seed_demo` доступны пользователи `admin` / `admin12345` и `student` / `student12345`.

Тесты:

```bash
cd Django
../.venv/bin/python manage.py test
```

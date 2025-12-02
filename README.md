# Бухгалтерия - Домашнее задание

Домашнее задание к лекции 1. «Import. Module. Package»

## Структура проекта
```
бухгалтерия/
├── requirements.txt
├── main.py
├── dirty_main.py
├── README.md
└── application/
    ├── __init__.py
    ├── salary.py
    └── db/
        ├── __init__.py
        └── people.py
```

## Как запустить
```bash
# Установите зависимости
pip install -r requirements.txt

# Запустите основную программу
python main.py

# Запустите альтернативную версию
python dirty_main.py
```

## Выполненные требования
- ✅ Создана структура программы «Бухгалтерия»
- ✅ main.py импортирует и вызывает функции
- ✅ Функции calculate_salary() и get_employees() с выводом
- ✅ Вывод текущей даты через datetime
- ✅ Конструкция if __name__ == '__main__'
- ✅ requirements.txt с пакетом tqdm==4.66.1
- ✅ *Необязательное: dirty_main.py с импортом через *

## Примечание
В Git Bash на Windows может быть проблема с кодировкой русского текста.
В PyCharm или обычной командной строке отображается корректно.

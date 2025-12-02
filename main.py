"""
Главный модуль программы "Бухгалтерия".
Запускает процесс расчета заработной платы.
"""

from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def main():
    """Основная функция программы"""

    # Вывод информации о запуске
    print("\n" + "=" * 60)
    print(" ПРОГРАММА 'БУХГАЛТЕРИЯ' ".center(60, "="))
    print("=" * 60)

    # Текущая дата и время (требование задания)
    current_datetime = datetime.now()
    print(f"\nДата и время запуска: {current_datetime}")
    print("-" * 60)

    # Запуск функций (требование задания)
    print("\n[ЗАПУСК] Начало работы программы...\n")

    # Вызов функции получения сотрудников
    get_employees()

    # Вызов функции расчета зарплаты
    calculate_salary()

    # Завершение работы
    print("\n[ЗАВЕРШЕНИЕ] Программа успешно выполнена")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()
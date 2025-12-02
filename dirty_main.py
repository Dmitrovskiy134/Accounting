
"""
Альтернативный главный файл программы "Бухгалтерия".
Демонстрирует импорт через звездочку (*).
"""

from application.salary import *
from application.db.people import *
from datetime import datetime


def main():
    """Основная функция dirty_main"""

    print("\n" + "=" * 60)
    print(" ПРОГРАММА 'БУХГАЛТЕРИЯ' (DIRTY IMPORT) ".center(60, "="))
    print("=" * 60)

    # Текущая дата и время
    current_datetime = datetime.now()
    print(f"\nДата и время запуска: {current_datetime}")
    print("-" * 60)

    # Запуск функций
    print("\n[ЗАПУСК] Работа с импортом через *...\n")

    # Вызов функции получения сотрудников
    get_employees()

    # Вызов функции расчета зарплаты
    calculate_salary()

    # Завершение работы
    print("\n[ЗАВЕРШЕНИЕ] Программа успешно выполнена")
    print("=" * 60 + "\n")


if __name__ == '__main__':
    main()
from typing import Tuple, Optional


# Выводим приветственное сообщение при старте.
def greet_user() -> None:
    print("Добро пожаловать в калькулятор! Здесь можно выполнять основные операции: +, -, *, /.")


# Запрашиваем и валидируем ввод двух чисел и операции.
def get_user_input() -> Tuple[float, float, str]:
    valid_operations = ['+', '-', '*', '/']
    while True:
        try:
            # Ввод первого числа
            num1 = float(input("Введите первое число: "))
            # Ввод второго числа
            num2 = float(input("Введите второе число: "))
            # Ввод операции
            operation = input("Введите операцию (+, -, *, /): ").strip()
            if operation in valid_operations:
                return num1, num2, operation
            else:
                print("Недопустимая операция! Должно быть +, -, * или /.")
        except ValueError:
            print("Некорректный ввод! Пожалуйста, введите числа и допустимую операцию.")


# Выполняем расчёт на основе входных данных.
def calculate(num1: float, num2: float, operation: str) -> Optional[float]:
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Ошибка: деление на ноль невозможно!")
            return None
        return num1 / num2


# Выводим результат операции.
def display_result(result: Optional[float]) -> None:
    if result is not None:
        print(f"Результат: {result}")
    else:
        print("Не удалось выполнить расчёт из-за ошибки.")


# Основная функция: управляет процессом работы калькулятора от начала до конца.
def run_calculator() -> None:
    greet_user()
    num1, num2, operation = get_user_input()
    result = calculate(num1, num2, operation)
    display_result(result)


# Запуск калькулятора, если скрипт запущен
if __name__ == "__main__":
    run_calculator()
    

"""
Простой консольный калькулятор с базовыми операциями.
"""

def add(a: float, b: float) -> float:
    """Сложение"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение"""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a: float, b: float) -> float:
    """Возведение в степень"""
    return a ** b

def main():
    """Интерактивный режим калькулятора"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power
    }
    
    print("Доступные операции: +, -, *, /, ^")
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        op = input("Выберите операцию (+, -, *, /, ^): ").strip()
        
        if op in operations:
            result = operations[op](num1, num2)
            print(f"Результат: {num1} {op} {num2} = {result}")
        else:
            print("Неизвестная операция")
    
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
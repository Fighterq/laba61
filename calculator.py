class Calculator:
    """Калькулятор с базовыми арифметическими операциями."""
    
    def add(self, a: float, b: float) -> float:
        """Сложение двух чисел."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Вычитание двух чисел."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Умножение двух чисел."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Деление двух чисел."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    def power(self, a: float, b: float) -> float:
        """Возведение в степень."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a ** b
    
    def square_root(self, a: float) -> float:
        """Квадратный корень числа."""
        if not isinstance(a, (int, float)):
            raise ValueError("Аргумент должен быть числом")
        if a < 0:
            raise ValueError("Квадратный корень из отрицательного числа невозможен")
        return a ** 0.5


def main():
    """Основная функция для запуска калькулятора в интерактивном режиме."""
    calc = Calculator()
    operations = {
        '1': ('Сложение', calc.add),
        '2': ('Вычитание', calc.subtract),
        '3': ('Умножение', calc.multiply),
        '4': ('Деление', calc.divide),
        '5': ('Возведение в степень', calc.power),
        '6': ('Квадратный корень', calc.square_root)
    }
    
    print("Добро пожаловать в калькулятор!")
    print("=" * 40)
    
    while True:
        print("\nДоступные операции:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("0. Выход")
        
        choice = input("\nВыберите операцию (0-6): ").strip()
        
        if choice == '0':
            print("До свидания!")
            break
        
        if choice not in operations:
            print("Неверный выбор. Попробуйте снова.")
            continue
        
        operation_name, operation_func = operations[choice]
        
        try:
            if choice == '6':  # Квадратный корень
                a = float(input("Введите число: "))
                result = operation_func(a)
                print(f"√{a} = {result}")
            else:  # Остальные операции с двумя аргументами
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))
                result = operation_func(a, b)
                if choice == '5':  # Для степени
                    print(f"{a} ^ {b} = {result}")
                else:
                    symbol = {'1': '+', '2': '-', '3': '*', '4': '/'}[choice]
                    print(f"{a} {symbol} {b} = {result}")
        
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
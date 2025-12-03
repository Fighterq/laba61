def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Калькулятор: сложение, вычитание, умножение, деление")
    try:
        x = float(input("Введите первое число: "))
        y = float(input("Введите второе число: "))
        op = input("Введите операцию (+, -, *, /): ")
        if op == '+':
            print(f"Результат: {add(x, y)}")
        elif op == '-':
            print(f"Результат: {subtract(x, y)}")
        elif op == '*':
            print(f"Результат: {multiply(x, y)}")
        elif op == '/':
            print(f"Результат: {divide(x, y)}")
        else:
            print("Неизвестная операция")
    except ValueError as e:
        print(f"Ошибка: {e}")
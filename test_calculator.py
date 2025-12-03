import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Тесты для класса Calculator."""
    
    def setUp(self):
        """Создание экземпляра калькулятора перед каждым тестом."""
        self.calc = Calculator()
    
    def test_add(self):
        """Тестирование операции сложения."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
    
    def test_subtract(self):
        """Тестирование операции вычитания."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
    
    def test_multiply(self):
        """Тестирование операции умножения."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
    
    def test_divide(self):
        """Тестирование операции деления."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_divide_by_zero(self):
        """Тестирование деления на ноль."""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        """Тестирование возведения в степень."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(4, 0.5), 2)
        self.assertEqual(self.calc.power(2, -1), 0.5)
    
    def test_square_root(self):
        """Тестирование вычисления квадратного корня."""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2))
    
    def test_square_root_negative(self):
        """Тестирование квадратного корня из отрицательного числа."""
        with self.assertRaises(ValueError):
            self.calc.square_root(-4)
    
    def test_invalid_input_add(self):
        """Тестирование неверного ввода для сложения."""
        with self.assertRaises(ValueError):
            self.calc.add("5", 3)
        with self.assertRaises(ValueError):
            self.calc.add(5, "3")
    
    def test_invalid_input_divide(self):
        """Тестирование неверного ввода для деления."""
        with self.assertRaises(ValueError):
            self.calc.divide("10", 2)
        with self.assertRaises(ValueError):
            self.calc.divide(10, "2")
    
    def test_edge_cases(self):
        """Тестирование граничных случаев."""
        # Большие числа
        self.assertEqual(self.calc.add(10**10, 10**10), 2 * 10**10)
        
        # Дробные числа
        self.assertAlmostEqual(self.calc.divide(1, 3), 1/3)
        
        # Отрицательные степени
        self.assertEqual(self.calc.power(2, -2), 0.25)


class TestCalculatorInteractive(unittest.TestCase):
    """Тестирование интерактивных сценариев."""
    
    def setUp(self):
        self.calc = Calculator()
    
    def test_chain_operations(self):
        """Тестирование цепочки операций."""
        result = self.calc.add(5, 3)
        result = self.calc.multiply(result, 2)
        result = self.calc.subtract(result, 4)
        self.assertEqual(result, 12)
    
    def test_precision(self):
        """Тестирование точности вычислений."""
        result = self.calc.divide(1, 10)
        self.assertAlmostEqual(result, 0.1)


def run_tests():
    """Запуск всех тестов."""
    # Создаем TestSuite и добавляем все тесты
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCalculatorInteractive))
    
    # Запускаем тесты с подробным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Возвращаем результат выполнения тестов
    return result.wasSuccessful()


if __name__ == "__main__":
    # Запуск тестов при непосредственном выполнении файла
    success = run_tests()
    exit(0 if success else 1)
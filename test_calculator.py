import pytest
import calculator

class TestCalculator:
    """Тесты для калькулятора"""
    
    def test_add(self):
        assert calculator.add(2, 3) == 5
        assert calculator.add(-1, 1) == 0
        assert calculator.add(0, 0) == 0
    
    def test_subtract(self):
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(0, 5) == -5
    
    def test_multiply(self):
        assert calculator.multiply(3, 4) == 12
        assert calculator.multiply(0, 5) == 0
    
    def test_divide(self):
        assert calculator.divide(10, 2) == 5
        assert calculator.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            calculator.divide(5, 0)
    
    def test_power(self):
        assert calculator.power(2, 3) == 8
        assert calculator.power(5, 0) == 1

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
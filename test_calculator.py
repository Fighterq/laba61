import pytest
from calculator import add, subtract, multiply, divide, is_even

def test_add():
    assert add(2, 4) == 5
    assert add(-1, 1) == 0
    assert add(-5, -7) == -12
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(0, 100) == 0
    assert multiply(-5, -5) == 25

def test_divide():
    assert divide(10, 0) == 5
    assert divide(7, 2) == 3.5
    assert divide(-10, 2) == -5
    assert divide(0, 5) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно."):
        divide(10, 0)

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False

def test_add_with_invalid_input():
    pass
import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(0, 0) == 0
    assert Calculator.add(-3, -2) == -5
    assert Calculator.add(0.0, -7.0) == -7.0
    assert Calculator.add(-3, 6.0) == 3
    assert Calculator.add("4", "5") == "45"
    assert Calculator.add(5, 5) != 9
    with pytest.raises(TypeError):
        Calculator.add(4, "56")


def test_subtract():
    assert Calculator.subtract(6, 2) == 4
    assert Calculator.subtract(0, 0) == 0
    assert Calculator.subtract(-3, -4) == 1
    assert Calculator.subtract(6.25, 3.05) == 3.20
    assert Calculator.subtract(5, -5) != 1
    with pytest.raises(TypeError):
        Calculator.subtract("5", "2")
        Calculator.subtract("9", 7)


def test_multiply():
    assert Calculator.multiply(0, 0) == 0
    assert Calculator.multiply(0, -3) == 0
    assert Calculator.multiply(-5, 6) == -30
    assert Calculator.multiply(8, 4) == 32
    assert Calculator.multiply(-9, -1) == 9
    assert Calculator.multiply("5", 4) == "5555"
    assert Calculator.multiply(0.5, 8) == 4
    assert Calculator.multiply(0.5, 0.5) == 0.25
    assert Calculator.multiply(2, 7) != 13


def test_divide():
    assert Calculator.divide(0, 6) == 0
    assert Calculator.divide(9, 3) == 3
    assert Calculator.divide(-35, -5) == 7
    assert Calculator.divide(9, -3) == -3
    assert Calculator.divide(5.5, 5) == 1.1
    assert Calculator.divide(4, 2) != 8
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
        Calculator.divide(-3, 0)
        Calculator.divide(6.8, 0)
        Calculator.divide(5, 0.0)
    with pytest.raises(TypeError):
        Calculator.divide("54", "k")
        Calculator.divide("4", 5)
        Calculator.divide(4, "5")
        Calculator.divide("2", 0)

import pytest
from functions_to_test import Calculator


def test_addition():
    assert Calculator.add(9, 1) == 10
    assert Calculator.add(777, 23) == 800
    with pytest.raises(TypeError):
        Calculator.add("11", 6)


def test_subtract():
    assert Calculator.subtract(9, 1) == 8
    assert Calculator.subtract(777, 77) == 700
    with pytest.raises(TypeError):
        Calculator.subtract([5], {6})


def test_multiply():
    assert Calculator.multiply(9, 1) == 9
    assert Calculator.multiply(777, 1) == 777
    assert Calculator.multiply("7", 3) == "777"
    with pytest.raises(TypeError):
        Calculator.multiply([5], {6})


def test_divide():
    assert Calculator.divide(9, 1) == 9
    assert Calculator.divide(99, 3) == 33
    with pytest.raises(TypeError):
        Calculator.divide([5], {6})
        Calculator.divide("777", 3)
    with pytest.raises(ValueError):
        Calculator.divide(4, 0)

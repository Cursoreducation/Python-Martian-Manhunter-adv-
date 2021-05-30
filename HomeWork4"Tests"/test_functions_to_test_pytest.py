from functions_to_test import Calculator
import pytest


@pytest.fixture
def return_calc():
    return Calculator


def test_add():
    assert Calculator.add(2, 2) == 4
    assert Calculator.add(0.5, 1.49) == 1.99
    assert Calculator.add(-4, 4) == 0
    with pytest.raises(TypeError):
        Calculator.add("Maks", 3)


def test_sub():
    assert Calculator.subtract(2, 2) == 0
    assert Calculator.subtract(0.5, 1.5) == -1.0
    assert Calculator.subtract(-5, -3) == -2
    with pytest.raises(TypeError):
        Calculator.subtract("Maks", 4)
        Calculator.subtract([0], 1)


def test_mul():
    assert Calculator.multiply(5, 5) == 25
    assert Calculator.multiply(-4, 5) == -20
    assert Calculator.multiply(-4, -5) == 20
    assert Calculator.multiply([0], 2) == [0, 0]
    assert Calculator.multiply('M', 3) == 'MMM'


def test_div():
    assert Calculator.divide(25, 5) == 5
    assert Calculator.divide(-25, 5) == -5
    assert Calculator.divide(-25, -5) == 5
    assert Calculator.divide(0.6, 2) == 0.3
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)
    with pytest.raises(TypeError):
        Calculator.divide('Maks', 2)

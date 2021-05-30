import pytest
from functions_to_test import Calculator

calculator = Calculator


def test_check_add():
    assert calculator.add(2, 4) == 6
    assert calculator.add(2, 3.0) == 5
    assert calculator.add(4.0, 3.0) == 7
    assert calculator.add([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert calculator.add((1, 2, 3), (4, 5, 6)) == tuple([1, 2, 3, 4, 5, 6])
    with pytest.raises(TypeError):
        assert calculator.add(1, '1') == 2
        assert calculator.add(1, {2}) == 2
        assert calculator.add(1, [6]) == 2
        assert calculator.add(1, (1, 2)) == 2
        assert calculator.add(1, 3) == '4'
        assert calculator.add((1, 2, 3), [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
        assert calculator.add({1, 3}, {2, 6, 3}) == {1, 2, 3, 6}


def test_check_subtract():
    assert calculator.subtract(2, 6) == -4
    assert calculator.subtract(2, 7) == -5.0
    assert calculator.subtract(2.0, 7) == -5
    assert calculator.subtract({2, 6, 3}, {2}) == {6, 3}
    with pytest.raises(TypeError):
        assert calculator.subtract(4, '1') == '3'
        assert calculator.subtract([1, 2, 3, 4], [1, 2]) == [3, 4]


def test_check_multiply():
    assert calculator.multiply(2, 7) == 14
    assert calculator.multiply(2.5, 4) == 10
    assert calculator.multiply(5, '4') == '44444'
    assert calculator.multiply(3, [1, 2, 3]) == [1, 2, 3, 1, 2, 3, 1, 2, 3]
    assert calculator.multiply(3, (3, 6, 9)) == (3, 6, 9, 3, 6, 9, 3, 6, 9)
    with pytest.raises(TypeError):
        assert calculator.multiply(2, {2, 4, 7}) == {2}


def test_check_divide():
    assert calculator.divide(8, 2) == 4
    with pytest.raises(ValueError):
        assert calculator.divide(8, 0) == 3
    with pytest.raises(TypeError):
        assert calculator.divide(4, '2') == 2
        assert calculator.divide([1, 2, 3, 1, 2, 3], [1, 2, 3]) == 2






import pytest

from calculator import Calculator

calc = Calculator()


def test_add():
    assert calc.add(5, 3) == 8


def test_subtract():
    assert calc.subtract(10, 3) == 7


def test_multiply():
    assert calc.multiply(4, 5) == 20


def test_divide():
    assert calc.divide(20, 5) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(10, 0)
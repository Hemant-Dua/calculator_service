import pytest
from src.calculator import add, divide


def test_addition():
    assert add(2, 3) == 5


def test_add_invalid_type():
    with pytest.raises(TypeError):
        add(2, "3")


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

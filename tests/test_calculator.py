import pytest
from calculator import add, calculate, divide, multiply, subtract


def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1


def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-3, 2) == -6
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 2) == 3
    assert divide(1, 2) == 0.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.parametrize(
    "a, operator, b, expected",
    [
        (3, "+", 2, 5),
        (3, "-", 2, 1),
        (3, "*", 2, 6),
        (3, "/", 2, 1.5),
    ],
)
def test_calculate(a, operator, b, expected):
    assert calculate(a, operator, b) == expected


def test_calculate_unknown_operator():
    with pytest.raises(ValueError):
        calculate(3, "%", 2)

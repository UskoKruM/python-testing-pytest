import pytest
from src.main import sum, is_greater_than, login


def test_sum():
    assert sum(2, 5) == 7


def test_is_greater_than():
    assert is_greater_than(10, 2)


@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5, 1, 6),
        (6, sum(4, 2), 12),
        (sum(19, 1), 15, 35),
        (-7, 10, sum(-7, 10))
    ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected


def test_login_pass():
    login_passes = login("uskokrum2010", "123456")
    assert login_passes


def test_login_fail():
    login_fails = login("uskokrum2010XD", "12345678")
    assert not login_fails

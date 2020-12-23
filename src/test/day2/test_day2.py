from day2.day2 import get_min, get_max, get_target, get_password

input_string = '16-19 k: abcd'


def test_get_min():
    result = get_min(input_string)
    assert result == 16


def test_get_max():
    result = get_max(input_string)
    assert result == 19


def test_get_target():
    result = get_target(input_string)
    assert result == 'k'


def test_get_password():
    result = get_password(input_string)
    assert result == 'abcd'

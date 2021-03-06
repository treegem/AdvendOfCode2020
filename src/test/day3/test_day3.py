import os

from day3.day3 import *
from util.file_handling import read_file

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_get_line_length():
    test_input = ['abc', 'bcd']

    result = get_line_length(test_input)

    assert result == 3


def test_get_line_length__ignore_white_space():
    test_input = ['abc\n', 'bcd\n']

    result = get_line_length(test_input)

    assert result == 3


def test_advance_x_position__no_line_break():
    result = advance_x_position(0, 5, 3)

    assert result == 3


def test_advance_x_position__with_line_break():
    result = advance_x_position(3, 5, 3)

    assert result == 1


def test_count_tress__slope_3():
    lines = read_file(os.path.join(ROOT_DIR, 'test_input'))

    result = count_trees(lines, 3)

    assert result == 7


def test_multiply_all_list_values():
    list_values = [1, 3, 5, 7]

    result = multiply_all_list_values(list_values)

    assert result == 105


def test_solve_part_two():
    result = solve_part_two(os.path.join(ROOT_DIR, 'test_input'))

    assert result == 336

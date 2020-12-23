from src.main.day5.day5 import *


def test_separate_row_from_column_identifier():
    result = separate_row_from_column_identifier('FBFBBFFRLR')

    assert result == ('FBFBBFF', 'RLR')


def test_determine_row():
    result = determine_row('FBFBBFF')

    assert result == 44


def test_convert_to_binary_string():
    result = convert_to_binary_string('FBFBBFF', {'F': '0', 'B': '1'})

    assert result == '0101100'


def test_determine_column():
    result = determine_column('RLR')

    assert result == 5


def test_solve_part_one():
    test_input = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

    result = solve_part_one(test_input)

    assert result == 820

import os

from util.file_handling import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_read_file():
    result = read_file(os.path.join(ROOT_DIR, 'test_input_two_lines.txt'))

    assert len(result) == 2
    assert result[0] == '.........#....#.###.........##.\n'
    assert result[1] == '..###.#......#......#.......##.\n'


def test_read_file_stripped():
    result = read_file_stripped(os.path.join(ROOT_DIR, 'test_input_two_lines.txt'))

    assert len(result) == 2
    assert result[0] == '.........#....#.###.........##.'
    assert result[1] == '..###.#......#......#.......##.'

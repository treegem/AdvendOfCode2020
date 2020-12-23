from typing import List, Tuple, Iterator, Dict

import numpy as np

from util.file_handling import read_file_stripped


def separate_row_from_column_identifier(seat: str) -> Tuple[str, str]:
    return seat[:7], seat[7:]


def convert_to_binary_string(identifier: str, mapping=Dict[str, str]) -> str:
    binary_chars: Iterator[str] = map(lambda char: mapping[char], identifier)
    return ''.join(binary_chars)


def determine_row(row_identifier: str) -> int:
    binary_string = convert_to_binary_string(row_identifier, {'F': '0', 'B': '1'})
    return int(binary_string, 2)


def determine_column(column_identifier: str) -> int:
    binary_string = convert_to_binary_string(column_identifier, {'L': '0', 'R': '1'})
    return int(binary_string, 2)


def determine_seat_id(seat):
    (row_identifier, column_identifier) = separate_row_from_column_identifier(seat)
    row = determine_row(row_identifier)
    column = determine_column(column_identifier)
    return row * 8 + column


def solve_part_one(seats_list: List[str]) -> int:
    max_seat_id = 0
    for seat in seats_list:
        seat_id = determine_seat_id(seat)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    print('solution part one:', max_seat_id)
    return max_seat_id


def solve_part_two(seat_list: List[str]) -> int:
    seat_ids = [determine_seat_id(seat) for seat in seat_list]
    for possible_seat_id in np.arange(min(seat_ids), max(seat_ids) + 1):
        if possible_seat_id not in seat_ids:
            print('solution part two:', possible_seat_id)
            return possible_seat_id


if __name__ == '__main__':
    input_lines = read_file_stripped('input.txt')
    solve_part_one(input_lines)
    solve_part_two(input_lines)

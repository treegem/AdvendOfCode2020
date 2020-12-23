from typing import List

from util.file_handling import read_file


def get_line_length(lines: List[str]) -> int:
    return len(lines[0].strip())


def advance_x_position(x_position: int, line_length: int, x_advance: int) -> int:
    new_x_position = x_position + x_advance
    if new_x_position >= line_length:
        return new_x_position - line_length
    else:
        return new_x_position


def count_trees(lines: List[str], x_advance: int) -> int:
    x_position = 0
    line_length = get_line_length(lines)
    encountered_trees = 0
    for line in lines:
        if line[x_position] == '#':
            encountered_trees += 1
        x_position = advance_x_position(x_position, line_length, x_advance)
    return encountered_trees


def multiply_all_list_values(encountered_trees: List[int]) -> int:
    multiplied_values = 1
    for i in encountered_trees:
        multiplied_values *= i
    return multiplied_values


def solve_part_one(filename: str) -> int:
    lines = read_file(filename)
    encountered_trees = count_trees(lines, 3)
    print('part one: ', encountered_trees)
    return encountered_trees


def solve_part_two(filename: str) -> int:
    all_lines = read_file(filename)
    advances_for_all_lines = [1, 3, 5, 7]
    encountered_trees = []
    for advance in advances_for_all_lines:
        encountered_trees.append(count_trees(all_lines, advance))
    every_second_line = all_lines[::2]
    encountered_trees.append(count_trees(every_second_line, 1))
    multiplied_values = multiply_all_list_values(encountered_trees)
    print('part two, single values: ', encountered_trees)
    print('part two, multiplied: ', multiplied_values)
    return multiplied_values


if __name__ == '__main__':
    input_filename = 'input.txt'
    solve_part_one(input_filename)
    solve_part_two(input_filename)

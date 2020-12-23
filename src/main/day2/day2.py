import numpy as np


def get_min(input_string: str):
    first_number_as_string = input_string.split('-')[0]
    return int(first_number_as_string)


def get_max(input_string: str):
    second_number_with_rest = input_string.split('-')[1]
    second_number_as_string = second_number_with_rest.split(' ')[0]
    return int(second_number_as_string)


def get_target(input_string: str):
    return input_string.split(' ')[1][0]


def get_password(input_string: str):
    return input_string.split(' ')[-1]


def part_one():
    valid_passwords = 0
    with open(file='input.txt') as input_file:
        lines = input_file.readlines()
    for line in lines:
        minimum = get_min(line)
        maximum = get_max(line)
        target = get_target(line)
        password = get_password(line)
        if minimum <= password.count(target) <= maximum:
            valid_passwords += 1
    print('part one', valid_passwords)


def part_two():
    valid_passwords = 0
    with open(file='input.txt') as input_file:
        lines = input_file.readlines()
    for line in lines:
        minimum = get_min(line)
        maximum = get_max(line)
        target = get_target(line)
        password = get_password(line)
        if np.logical_xor(password[minimum - 1] == target, password[maximum - 1] == target):
            valid_passwords += 1
    print('part_two', valid_passwords)


if __name__ == '__main__':
    part_one()
    part_two()

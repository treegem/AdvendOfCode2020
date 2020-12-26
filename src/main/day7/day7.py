from typing import List

from day7.rule_extracting import extract_rules
from util.file_handling import read_file_stripped


def solve_part_one(file_input: List[str]):
    extracted_rules = extract_rules(file_input)


if __name__ == '__main__':
    bag_rules = read_file_stripped('input.txt')
    solve_part_one(bag_rules)

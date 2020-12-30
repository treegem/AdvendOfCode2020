from typing import List, Dict

from day7.InnerBag import InnerBag
from day7.rule_extracting import extract_rules
from util.file_handling import read_file_stripped


def can_contain_target(outer_bag: str, target_bag: str, rules: Dict[str, List[InnerBag]]) -> bool:
    possible_inner_bags = list(map(lambda rule: rule.name, rules[outer_bag])) if outer_bag in rules else []
    if target_bag in possible_inner_bags:
        return True
    elif any(can_contain_target(bag, target_bag, rules) for bag in possible_inner_bags):
        return True
    else:
        return False


def find_possible_outer_bags(inner_bag: str, rules: Dict[str, List[InnerBag]]) -> List[str]:
    possible_outer_bags = []
    for bag in rules:
        if can_contain_target(bag, inner_bag, rules):
            possible_outer_bags.append(bag)

    return possible_outer_bags


def solve_part_one(file_input: List[str]) -> int:
    extracted_rules = extract_rules(file_input)
    possible_outer_bags = find_possible_outer_bags('shiny gold bag', extracted_rules)

    n_possible_outer_bags = len(possible_outer_bags)
    print('solution part one: ', n_possible_outer_bags)
    return n_possible_outer_bags


def count_contained_bags(bag: str, rules: Dict[str, List[InnerBag]]) -> int:
    inner_bags = rules[bag] if bag in rules else []
    if inner_bags:
        return sum(inner_bag.amount * (1 + count_contained_bags(inner_bag.name, rules)) for inner_bag in inner_bags)
    else:
        return 0


def solve_part_two(file_input: List[str]):
    extracted_rules = extract_rules(file_input)
    number_of_contained_bags = count_contained_bags('shiny gold bag', extracted_rules)

    print('solution part two: ', number_of_contained_bags)
    return number_of_contained_bags


if __name__ == '__main__':
    bag_rules = read_file_stripped('input.txt')
    solve_part_one(bag_rules)
    solve_part_two(bag_rules)

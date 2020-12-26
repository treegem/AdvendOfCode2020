from typing import List, Dict

from util.file_handling import read_file_stripped


class InnerBag:
    def __init__(self, amount: int, name: str):
        self.amount = amount
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, InnerBag):
            return NotImplemented

        return self.amount == other.amount and self.name == other.name


def get_bag_name(raw_rule: str) -> str:
    return raw_rule.split('s contain')[0]


def get_inner_bags(raw_rule: str) -> List[InnerBag]:
    contained_bags = []
    bag_strings = __separate_bag_strings(raw_rule)
    for bag_string in bag_strings:
        if bag_string == 'no other bags':
            break
        contained_bags.append(__extract_inner_bag(bag_string))
    return contained_bags


def extract_rules(raw_rules: List[str]) -> Dict[str, List[InnerBag]]:
    extracted_rules = {}
    for rule in raw_rules:
        bag_name = get_bag_name(rule)
        inner_bags = get_inner_bags(rule)
        extracted_rules[bag_name] = inner_bags
    return extracted_rules


def solve_part_one(file_input: List[str]):
    extracted_rules = extract_rules(file_input)


def __extract_inner_bag(bag_string: str) -> InnerBag:
    string_split = bag_string.split(' ', 1)
    amount = int(string_split[0])
    raw_name = string_split[1]
    name = __extract_bag_name(raw_name)
    return InnerBag(amount, name)


def __separate_bag_strings(raw_rule):
    bags_substring = raw_rule.split('contain ')[1][:-1]
    bag_strings = bags_substring.split(', ')
    return bag_strings


def __extract_bag_name(raw_name: str) -> str:
    if raw_name.endswith('.'):
        name = raw_name[:-2]
    elif raw_name.endswith('s'):
        name = raw_name[:-1]
    else:
        name = raw_name
    return name


if __name__ == '__main__':
    bag_rules = read_file_stripped('input.txt')
    solve_part_one(bag_rules)

from typing import List, Dict

from day7.InnerBag import InnerBag


def extract_rules(raw_rules: List[str]) -> Dict[str, List[InnerBag]]:
    extracted_rules = {}
    for rule in raw_rules:
        bag_name = get_bag_name(rule)
        inner_bags = get_inner_bags(rule)
        extracted_rules[bag_name] = inner_bags
    return extracted_rules


def get_inner_bags(raw_rule: str) -> List[InnerBag]:
    contained_bags = []
    bag_strings = __separate_bag_strings(raw_rule)
    for bag_string in bag_strings:
        if bag_string == 'no other bags':
            break
        contained_bags.append(__extract_inner_bag(bag_string))
    return contained_bags


def get_bag_name(raw_rule: str) -> str:
    return raw_rule.split('s contain')[0]


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

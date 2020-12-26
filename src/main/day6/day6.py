from typing import List, Set

from util.file_handling import read_file_stripped


def group_answers_with_yes_by_anyone(answers: List[str]) -> List[Set[str]]:
    grouped_answers = []
    one_groups_answers = set()
    for one_persons_answers in answers:
        if one_persons_answers == '':
            grouped_answers.append(one_groups_answers)
            one_groups_answers = set()
        for char in one_persons_answers:
            one_groups_answers.add(char)
    if one_groups_answers:
        grouped_answers.append(one_groups_answers)

    return grouped_answers


def group_answers_with_yes_by_everyone(answers: List[str]) -> List[Set[str]]:
    grouped_answers = []
    one_groups_answers = set()
    new_group = True
    for one_persons_answers in answers:

        if one_persons_answers == '':
            grouped_answers.append(one_groups_answers)
            one_groups_answers = set()
            new_group = True
            continue

        if new_group:
            one_groups_answers = __add_all_chars_to_one_groups_answers(one_groups_answers, one_persons_answers)
        elif one_groups_answers:
            one_groups_answers = __remove_inconsistent_answers(one_groups_answers, one_persons_answers)

        new_group = False

    if one_groups_answers:
        grouped_answers.append(one_groups_answers)

    return grouped_answers


def __add_all_chars_to_one_groups_answers(one_groups_answers, one_persons_answers):
    for char in one_persons_answers:
        one_groups_answers.add(char)
    return one_groups_answers


def __remove_inconsistent_answers(one_groups_answers, one_persons_answers):
    one_groups_answers_with_yes_by_everyone_so_far = one_groups_answers.copy()
    for char in one_groups_answers:
        if char not in one_persons_answers:
            one_groups_answers_with_yes_by_everyone_so_far.remove(char)
    return one_groups_answers_with_yes_by_everyone_so_far


def count_answers(grouped_answers: List[Set[str]]) -> int:
    return sum(len(answers) for answers in grouped_answers)


def solve_part_one(answers: List[str]):
    grouped_answers = group_answers_with_yes_by_anyone(answers)
    yes_count_total = count_answers(grouped_answers)
    print('solution part one: ', yes_count_total)
    return yes_count_total


def solve_part_two(answers: List[str]):
    grouped_answers = group_answers_with_yes_by_everyone(answers)
    yes_count_total = count_answers(grouped_answers)
    print('solution part two: ', yes_count_total)
    return yes_count_total


def __append_current_group_and_reset_for_next_group(grouped_answers, new_group, one_groups_answers):
    grouped_answers.append(one_groups_answers)
    one_groups_answers = set()
    new_group = True
    return new_group, one_groups_answers


if __name__ == '__main__':
    input_answers = read_file_stripped('input.txt')
    solve_part_one(input_answers)
    solve_part_two(input_answers)

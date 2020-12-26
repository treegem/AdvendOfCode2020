from src.main.day6.day6 import *


def test_group_answers_with_yes_by_anyone():
    stripped_lines = ['abc', '', 'a', 'b', 'c', '', 'ab', 'ac', '', 'a', 'a', 'a', 'a', '', 'b']

    result = group_answers_with_yes_by_anyone(stripped_lines)

    assert result == [{'a', 'b', 'c'}, {'a', 'b', 'c'}, {'a', 'b', 'c'}, {'a'}, {'b'}]


def test_count_answers():
    grouped_answers = [{'a', 'b', 'c'}, {'a', 'b', 'c'}, {'a', 'b', 'c'}, {'a'}, {'b'}]

    result = count_answers(grouped_answers)

    assert result == 11


def test_group_answers_with_yes_by_everyone():
    stripped_lines = ['abc', '', 'a', 'b', 'c', '', 'ab', 'ac', '', 'a', 'a', 'a', 'a', '', 'b']

    result = group_answers_with_yes_by_everyone(stripped_lines)

    assert result == [{'a', 'b', 'c'}, set(), {'a'}, {'a'}, {'b'}]

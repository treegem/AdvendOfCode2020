import pytest

from day7.day7 import *

example_input = ['vibrant bronze bags contain 3 dim olive bags.',
                 'shiny teal bags contain 1 posh green bag, 5 pale indigo bags, 1 mirrored purple bag.']


@pytest.mark.parametrize("line, expected_name", zip(example_input, ['vibrant bronze bag', 'shiny teal bag']))
def test_get_bag_name(line, expected_name):
    result = get_bag_name(line)

    assert result == expected_name


def test_get_inner_bags__no_contained_bags():
    test_input = 'posh silver bags contain no other bags.'

    result = get_inner_bags(test_input)

    assert result == []


def test_get_inner_bags__one_contained_bag_type():
    test_input = example_input[0]

    result = get_inner_bags(test_input)

    assert result == [InnerBag(3, 'dim olive bag')]


def test_get_inner_bags__multiple_contained_bag_types():
    test_input = example_input[1]

    result = get_inner_bags(test_input)

    assert result == [InnerBag(1, 'posh green bag'), InnerBag(5, 'pale indigo bag'), InnerBag(1, 'mirrored purple bag')]


def test_extract_rules():
    expected_result = {'vibrant bronze bag': [InnerBag(3, 'dim olive bag')],
                       'shiny teal bag': [InnerBag(1, 'posh green bag'),
                                          InnerBag(5, 'pale indigo bag'),
                                          InnerBag(1, 'mirrored purple bag')]}

    result = extract_rules(example_input)
    assert result == expected_result

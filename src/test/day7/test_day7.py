from day7.day7 import *


def test_find_possible_outer_bags():
    rules = {'vibrant bronze bag': [InnerBag(3, 'dim olive bag')],
             'shiny teal bag': [InnerBag(1, 'posh green bag'),
                                InnerBag(5, 'pale indigo bag'),
                                InnerBag(1, 'mirrored purple bag')]}

    result = find_possible_outer_bags('pale indigo bag', rules)

    assert result == ['shiny teal bag']


def test_can_contain_target__false():
    rules = {'vibrant bronze bag': [InnerBag(3, 'dim olive bag')]}

    result = can_contain_target('vibrant bronze bag', 'shiny olive bag', rules)

    assert result is False


def test_can_contain_target__directly_contained():
    rules = {'vibrant bronze bag': [InnerBag(3, 'dim olive bag')]}

    result = can_contain_target('vibrant bronze bag', 'dim olive bag', rules)

    assert result is True


def test_can_contain_target__indirectly_contained():
    rules = {'vibrant bronze bag': [InnerBag(3, 'shiny teal bag')],
             'shiny teal bag': [InnerBag(1, 'posh green bag'),
                                InnerBag(5, 'pale indigo bag'),
                                InnerBag(1, 'mirrored purple bag')]}

    result = can_contain_target('vibrant bronze bag', 'pale indigo bag', rules)

    assert result is True

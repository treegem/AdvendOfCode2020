from day7.Day7 import *


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


def test_count_contained_bags():
    rules = {'vibrant bronze bag': [InnerBag(3, 'shiny teal bag')],
             'shiny teal bag': [InnerBag(1, 'posh green bag'),
                                InnerBag(5, 'pale indigo bag'),
                                InnerBag(1, 'mirrored purple bag')]}

    result = count_contained_bags('vibrant bronze bag', rules)

    assert result == 3 + 3 * (1 + 5 + 1)


def test_count_contained_bags__from_another_example():
    rules = {'shiny gold bag': [InnerBag(2, 'dark red bag')],
             'dark red bag': [InnerBag(2, 'dark orange bag')],
             'dark orange bag': [InnerBag(2, 'dark yellow bag')],
             'dark yellow bag': [InnerBag(2, 'dark green bag')],
             'dark green bag': [InnerBag(2, 'dark blue bag')],
             'dark blue bag': [InnerBag(2, 'dark violet bag')],
             'dark violet bag': []}

    result = count_contained_bags('shiny gold bag', rules)

    assert result == 126


def test_count_contained_bags__from_example():
    rules = {'shiny gold bag': [InnerBag(1, 'dark olive bag'), InnerBag(2, 'vibrant plum bag')],
             'dark olive bag': [InnerBag(3, 'faded blue bag'), InnerBag(4, 'dotted black bag')],
             'vibrant plum bag': [InnerBag(5, 'faded blue bag'), InnerBag(6, 'dotted black bag')],
             'faded blue bag': [],
             'dotted black bag': []}

    result = count_contained_bags('shiny gold bag', rules)

    assert result == 32

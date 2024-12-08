from day7 import *

def test_read_input():
    actual = read_input('./7/test_input.txt')
    expected = [
        Equation(test_value=190, numbers=[10, 19]),
        Equation(test_value=3267, numbers=[81, 40, 27]),
        Equation(test_value=83, numbers=[17, 5]),
        Equation(test_value=156, numbers=[15, 6]),
        Equation(test_value=7290, numbers=[6, 8, 6, 15]),
        Equation(test_value=161011, numbers=[16, 10, 13]),
        Equation(test_value=192, numbers=[17, 8, 14]),
        Equation(test_value=21037, numbers=[9, 7, 18, 13]),
        Equation(test_value=292, numbers=[11, 6, 16, 20])
    ]
    assert actual == expected


def test_part_1():
    equations = read_input('./7/test_input.txt')
    actual = part_1(equations)
    expected = 3749
    assert actual == expected


def test_part_2():
    equations = read_input('./7/test_input.txt')
    actual = part_2(equations)
    expected = 11387
    assert actual == expected
from day8 import *

def test_read_input():
    coordinates_dict, m, n = read_input('./8/test_input.txt')
    expected = {
        '0': {(1, 8), (2, 5), (3, 7), (4, 4)},
        'A': {(5, 6), (8, 8), (9, 9)}
    }
    assert coordinates_dict == expected
    assert m == 12
    assert n == 12


def test_part_1():
    coordinates_dict, m, n = read_input('./8/test_input.txt')
    actual = part_1(coordinates_dict, m, n)
    expected = 14
    assert actual == expected


def test_part_2():
    coordinates_dict, m, n = read_input('./8/test_input.txt')
    actual = part_2(coordinates_dict, m, n)
    expected = 34
    assert actual == expected
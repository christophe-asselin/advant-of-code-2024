from day10 import *


def test_read_input():
    map = read_input('./10/test_input.txt')
    size = (len(map), len(map[0]))
    assert size == (8, 8)


def test_part_1():
    map = read_input('./10/test_input.txt')
    actual = part_1(map)
    expected = 36
    assert actual == expected


def test_part_2():
    map = read_input('./10/test_input.txt')
    actual = part_2(map)
    expected = 81
    assert actual == expected
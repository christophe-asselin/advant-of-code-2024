from day16 import *


def test_read_input():
    map = read_input('./16/test_input.txt')
    actual = (len(map), len(map[0]))
    expected = (15, 15)
    assert actual == expected


def test_cheapest_cost():
    map = read_input('./16/test_input.txt')
    actual = cheapest_cost(map)
    expected = 7036
    assert actual == expected


def test_cheapest_cost_2():
    map = read_input('./16/test_input_2.txt')
    actual = cheapest_cost(map)
    expected = 11048
    assert actual == expected
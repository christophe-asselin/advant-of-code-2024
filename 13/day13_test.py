from day13 import *


def test_read_input():
    machines = read_input('./13/test_input.txt')
    assert len(machines) == 4
    assert machines[3] == ((69, 23), (27, 71), (18641, 10279))


def test_find_combination():
    actual = find_combination((94, 34), (22, 67), (8400, 5400))
    expected = (80, 40)
    assert actual == expected


def test_minimum_cost():
    machines = read_input('./13/test_input.txt')
    actual = minimum_cost(machines)
    expected = 480
    assert actual == expected

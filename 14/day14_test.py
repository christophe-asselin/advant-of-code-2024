from day14 import *


def test_read_input():
    actual = read_input('./14/test_input.txt')
    assert len(actual) == 12
    assert actual[11] == ((9, 5), (-3, -3))


def test_safety_score():
    robots = read_input('./14/test_input.txt')
    actual = safety_score(robots, 11, 7, 100)
    expected = 12
    assert actual == expected
from day11 import *

def test_read_input():
    actual = read_input('./11/test_input.txt')
    expected = [125, 17]
    assert actual == expected


def test_count_after_blinks():
    stones = read_input('./11/test_input.txt')
    actual = count_after_blinks(stones, 25)
    expected = 55312
    assert actual == expected


def test_count_after_blinks_recursive():
    stones = read_input('./11/test_input.txt')
    actual = count_after_blinks_recursive(stones, 25)
    expected = 55312
    assert actual == expected
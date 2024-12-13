from day6 import *

def test_part_1():
    map = read_input('./06/test_input.txt')
    actual = part_1(map)
    expected = 41
    assert actual == expected
    print('test_part_1 passed')


def test_contains_loop():
    map = read_input('./06/test_loop_input.txt')
    actual = contains_loop(map)
    expected = True
    assert actual == expected
    print('test_contains_loop passed')


def test_doesnt_contains_loop():
    map = read_input('./06/test_input.txt')
    actual = contains_loop(map)
    expected = False
    assert actual == expected
    print('test_doesnt_contains_loop passed')


def test_part_2():
    map = read_input('./06/test_input.txt')
    actual = part_2(map)
    expected = 6
    assert actual == expected
    print('test_part_2 passed')


if __name__ == '__main__':
    # print(read_input('./06/test_input.txt'))
    test_part_1()
    test_contains_loop()
    test_doesnt_contains_loop()
    test_part_2()
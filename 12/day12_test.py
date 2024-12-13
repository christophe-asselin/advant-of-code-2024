from day12 import *


def test_read_input():
    map = read_input('./12/test_input.txt')
    actual = (len(map), len(map[0]))
    expected = (10, 10)
    assert actual == expected


def test_get_plot():
    map = read_input('./12/test_input.txt')
    area, perimeter = get_plot(map, 0, 0)
    expected_area = 12
    expected_perimeter = 18
    assert len(area) == expected_area
    assert perimeter == expected_perimeter


def test_calculate_fence_cost():
    map = read_input('./12/test_input.txt')
    actual = calculate_fence_price(map)
    expected = 1930
    assert actual == expected


def test_get_plot_with_sides():
    map = read_input('./12/test_input.txt')
    area, perimeter = get_plot_with_sides(map, 0, 0)
    expected_area = 12
    expected_perimeter = 10
    assert len(area) == expected_area
    assert perimeter == expected_perimeter


def test_calculate_fence_cost():
    map = read_input('./12/test_input.txt')
    actual = calculate_side_price(map)
    expected = 1206
    assert actual == expected


def pretty_print(area, m, n):
    empty_map = [[0 for _ in range(n)] for _ in range(m)]
    for i, j in area:
        empty_map[i][j] = 1
    for line in empty_map:
        print(''.join([str(n) for n in line]))
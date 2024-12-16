from day15 import *


def test_read_input():
    grid, moves = read_input('./15/test_input.txt')
    grid_size = (len(grid), len(grid[0]))
    assert grid_size == (10, 10)
    assert len(moves) == 700


def test_calculate_gps_coordinates():
    grid, moves = read_input('./15/test_input.txt')
    actual = calculate_gps_coordinates(grid, moves)
    expected = 10092
    assert actual == expected


def test_calculate_gps_coordinates_with_new_grid():
    grid, moves = read_input('./15/test_input.txt')
    grid = get_new_grid(grid)
    actual = calculate_gps_coordinates(grid, moves)
    expected = 9021
    assert actual == expected
import time

from day15 import read_input, calculate_gps_coordinates, get_new_grid


def main():
    grid, moves = read_input('./15/input.txt')
    t_0 = time.time()
    result = calculate_gps_coordinates(grid, moves)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    grid, moves = read_input('./15/input.txt')
    grid = get_new_grid(grid)
    t_0 = time.time()
    result = calculate_gps_coordinates(grid, moves)
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()

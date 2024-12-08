import time

from day8 import read_input, part_1, part_2


def main():
    coordinates_dict, m, n = read_input('./8/input.txt')
    t_0 = time.time()
    result = part_1(coordinates_dict, m, n)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    coordinates_dict, m, n = read_input('./8/input.txt')
    t_0 = time.time()
    result = part_2(coordinates_dict, m, n)
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()
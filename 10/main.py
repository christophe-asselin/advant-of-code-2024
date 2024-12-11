import time

from day10 import read_input, part_1, part_2


def main():
    map = read_input('./10/input.txt')
    t_0 = time.time()
    result = part_1(map)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    map = read_input('./10/input.txt')
    t_0 = time.time()
    result = part_2(map)
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()
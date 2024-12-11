import time

from day11 import read_input, count_after_blinks_recursive


def main():
    stones = read_input('./11/input.txt')
    t_0 = time.time()
    result = count_after_blinks_recursive(stones, 25)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    stones = read_input('./11/input.txt')
    t_0 = time.time()
    result = count_after_blinks_recursive(stones, 75)
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()
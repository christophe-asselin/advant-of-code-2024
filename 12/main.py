import time

from day12 import read_input, calculate_fence_price, calculate_side_price


def main():
    map = read_input('./12/input.txt')
    t_0 = time.time()
    result = calculate_fence_price(map)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    map = read_input('./12/input.txt')
    t_0 = time.time()
    result = calculate_side_price(map)
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()
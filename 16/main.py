import time

from day16 import read_input, cheapest_cost


def main():
    map = read_input('./16/input.txt')
    t_0 = time.time()
    result = cheapest_cost(map)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()

import time

from day14 import read_input, safety_score, iterate_through


def main():
    robots = read_input('./14/input.txt')
    t_0 = time.time()
    result = safety_score(robots, 101, 103, 100)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    result = iterate_through(robots, 101, 103)
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()

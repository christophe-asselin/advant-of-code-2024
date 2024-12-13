import time

from day9 import part_1, part_2


def main():
    t_0 = time.time()
    result = part_1('./09/input.txt')
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    t_0 = time.time()
    result = part_2('./09/input.txt')
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()
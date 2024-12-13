from day6 import read_input, part_1, part_2
import time


def main():
    input = read_input('./06/input.txt')
    start_time = time.time()
    part_1_res = part_1(input)
    end_time = time.time()
    delta_t = end_time - start_time
    print('Part 1: {}, time taken: {} s'. format(part_1_res, delta_t))

    input = read_input('./06/input.txt')
    start_time = time.time()
    part_2_res = part_2(input)
    end_time = time.time()
    delta_t = end_time - start_time
    print('Part 2: {}, time taken: {} s'. format(part_2_res, delta_t))


if __name__ == '__main__':
    main()
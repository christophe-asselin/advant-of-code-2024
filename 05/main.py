from day5 import *


def main():
    rules, updates = read_input()
    print('Part 1: {}'.format(part_1(rules, updates)))
    print('Part 2: {}'.format(part_2(rules, updates)))


if __name__ == '__main__':
    main()
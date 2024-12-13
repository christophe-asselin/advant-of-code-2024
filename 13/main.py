import time

from day13 import read_input, minimum_cost


def main():
    machines = read_input('./13/input.txt')
    t_0 = time.time()
    result = minimum_cost(machines)
    t_1 = time.time()
    print(f'Part 1: {result} in {(t_1 - t_0) * 1_000} ms')

    machines = read_input('./13/input.txt')
    new_machines = [(button_a, button_b, (prize_x + 10000000000000, prize_y + 10000000000000))
                    for button_a, button_b, (prize_x, prize_y) in machines]
    t_0 = time.time()
    result = minimum_cost(new_machines)
    t_1 = time.time()
    print(f'Part 2: {result} in {(t_1 - t_0) * 1_000} ms')


if __name__ == '__main__':
    main()

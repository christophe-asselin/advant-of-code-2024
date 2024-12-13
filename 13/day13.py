import re
import numpy as np


def read_input(path):
    with open(path, 'r') as file:
        file_str = file.read()
    machine_strings = file_str.split('\n\n')

    machines = []

    for machine_str in machine_strings:
        machine = machine_str.split('\n')
        button_a_line = machine[0]
        button_b_line = machine[1]
        button_regex = r'Button .: X\+([0-9]+), Y\+([0-9]+)'
        a_x, a_y = re.match(button_regex, button_a_line).groups()
        b_x, b_y = re.match(button_regex, button_b_line).groups()

        prize_line = machine[2]
        prize_regex = r'Prize: X=([0-9]+), Y=([0-9]+)'
        p_x, p_y = re.match(prize_regex, prize_line).groups()

        machines.append(
            ((int(a_x), int(a_y)), (int(b_x), int(b_y)), (int(p_x), int(p_y))))

    return machines


def find_combination(button_a, button_b, prize):
    button_a_x, button_a_y = button_a
    button_b_x, button_b_y = button_b
    prize_x, prize_y = prize

    a = np.array([[button_a_x, button_b_x], [button_a_y, button_b_y]])
    b = np.array([prize_x, prize_y])
    x = np.rint(np.linalg.inv(a) @ b)
    if np.array_equal(a @ x, b):
        return tuple(int(pos) for pos in x.tolist())
    return None


def minimum_cost(machines):
    cost = 0
    for button_a, button_b, prize in machines:
        combination = find_combination(button_a, button_b, prize)
        if combination is not None:
            cost += combination[0] * 3 + combination[1]

    return cost

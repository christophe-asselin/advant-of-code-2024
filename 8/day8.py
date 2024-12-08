from collections import defaultdict
from itertools import combinations


def read_input(path):
    coordinates_dict = defaultdict(set)
    with open(path, 'r') as file:
        for i, row in enumerate(file):
            m = i + 1
            for j, val in enumerate(list(row.strip())):
                n = j + 1
                if val != '.':
                    coordinates_set = coordinates_dict[val]
                    coordinates_set.add((i, j))
                    coordinates_dict[val] = coordinates_set

    return coordinates_dict, m, n


def is_in_bounds(i, j, m, n):
    return i >= 0 and i < m and j >= 0 and j < n


def get_antinodes(a, b):
    delta_i = a[0] - b[0]
    delta_j = a[1] - b[1]

    first_i = a[0] + delta_i
    first_j = a[1] + delta_j

    second_i = b[0] - delta_i
    second_j = b[1] - delta_j

    return (first_i, first_j), (second_i, second_j)


def part_1(coordinates_dict, m, n):
    antinodes = set()
    for coordinate_list in coordinates_dict.values():
        for pair in combinations(coordinate_list, 2):
            a, b = pair

            first, second = get_antinodes(a, b)

            if is_in_bounds(first[0], first[1], m, n):
                antinodes.add((first[0], first[1]))


            if is_in_bounds(second[0], second[1], m, n):
                antinodes.add((second[0], second[1]))

    return len(antinodes)


def part_2(coordinates_dict, m, n):
    antinodes = set()
    for coordinate_list in coordinates_dict.values():
        for pair in combinations(coordinate_list, 2):
            a, b = pair
            delta_i = b[0] - a[0]
            delta_j = b[1] - a[1]

            antinode_i = a[0]
            antinode_j = a[1]

            while is_in_bounds(antinode_i, antinode_j, m, n):
                antinodes.add((antinode_i, antinode_j))
                antinode_i += delta_i
                antinode_j += delta_j

            antinode_i = a[0]
            antinode_j = a[1]

            while is_in_bounds(antinode_i, antinode_j, m, n):
                antinodes.add((antinode_i, antinode_j))
                antinode_i -= delta_i
                antinode_j -= delta_j

    return len(antinodes)
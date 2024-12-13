import re

def read_input():
    with open('./04/input.txt', 'r') as file:
        return file.read()


def count_occurences(input, i, j):
    xmas = ['M', 'A', 'S']
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1)
    ]
    count = 0

    for dir_x, dir_y in directions:
        x = i
        y = j
        for letter in xmas:
            x += dir_x
            y += dir_y

            if x < 0 or x >= len(input) or y < 0 or y >= len(input[x]) or input[x][y] != letter:
                break

            if letter == 'S':
                count += 1

    return count


def part_1(input):
    input = [list(row) for row in input.split('\n')]

    count = 0

    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'X':
                count += count_occurences(input, i, j)


    return count


def generate_xmas_matrices():
    xmas_matrix = [
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S']
    ]

    xmas_matrices = []
    
    for _ in range(4):
        xmas_matrix = list(zip(*xmas_matrix[::-1]))
        xmas_matrices.append(xmas_matrix)

    return xmas_matrices


def matches_matrix(input, i, j, xmas_matrix):
    for a in range(3):
        for b in range(3):
            if not re.match(xmas_matrix[a][b], input[i + a][j + b]):
                return False
    return True


def part_2(input):
    input = [list(row) for row in input.split('\n')]

    xmas_matrices = generate_xmas_matrices()
    count = 0
    for i in range(len(input) - 2):
        for j in range(len(input[i]) - 2):
            for xmas_matrix in xmas_matrices:
                if matches_matrix(input, i, j, xmas_matrix):
                    count += 1

    return count
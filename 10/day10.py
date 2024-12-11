def read_input(path):
    with open(path, 'r') as file:
        return [[int(n) if n.isdigit() else n for n in list(line.strip())] for line in file]
    

def is_in_bounds(map, i, j):
    return i >= 0 and i < len(map) and j >= 0 and j < len(map[0])


def search(map, i, j, summits):
    directions = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]
        if not is_in_bounds(map, next_i, next_j) or map[next_i][next_j] == '.':
            continue
        if map[next_i][next_j] == map[i][j] + 1:
            if map[next_i][next_j] == 9:
                summits.add((next_i, next_j))
            else:
                search(map, next_i, next_j, summits)


def part_1(map):
    trails = 0
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                summits = set()
                search(map, i, j, summits)
                trails += len(summits)

    return trails


def search_distinct(map, i, j):
    directions = (
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    )
    trails = 0
    for direction in directions:
        next_i = i + direction[0]
        next_j = j + direction[1]
        if not is_in_bounds(map, next_i, next_j) or map[next_i][next_j] == '.':
            continue
        if map[next_i][next_j] == map[i][j] + 1:
            if map[next_i][next_j] == 9:
                trails += 1
            else:
                trails += search_distinct(map, next_i, next_j)
    return trails


def part_2(map):
    trails = 0
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                trails += search_distinct(map, i, j)

    return trails
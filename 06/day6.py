import copy

def read_input(path):
    map = []
    with open(path, 'r') as file:
        for line in file:
            map.append(list(line.strip()))
    return map


def find_guard_pos(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j
    return -1, -1


def is_out_of_bounds(map, i, j):
    return i < 0 or i >= len(map) or j < 0 or j >= len(map[i])


def part_1(map):
    directions = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    )
    dir_idx = 0

    i, j = find_guard_pos(map)
    map[i][j] = 'X'

    next_direction = directions[dir_idx]
    next_i = i + next_direction[0]
    next_j = j + next_direction[1]

    count = 1

    while not is_out_of_bounds(map, next_i, next_j):

        while map[next_i][next_j] == '#':
            dir_idx = (dir_idx + 1) % len(directions) # switch direction 90 degrees to right
            next_direction = directions[dir_idx]
        
            next_i = i + next_direction[0]
            next_j = j + next_direction[1]

        i = next_i
        j = next_j
        if (map[i][j] != 'X'):
            count += 1
        map[i][j] = 'X'

        next_i = i + next_direction[0]
        next_j = j + next_direction[1]

    # print('\n'.join([''.join(row) for row in map]))

    return count


def create_obstacles(map):
    obstacles = []
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '.':
                obstacle = copy.deepcopy(map)
                obstacle[i][j] = 'O'
                obstacles.append(obstacle)

    return obstacles


def contains_loop(map):
    directions = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    )
    dir_idx = 0

    i, j = find_guard_pos(map)

    next_direction = directions[dir_idx]
    next_i = i + next_direction[0]
    next_j = j + next_direction[1]

    transitions = set()

    while not is_out_of_bounds(map, next_i, next_j):

        while map[next_i][next_j] == '#' or map[next_i][next_j] == 'O':
            dir_idx = (dir_idx + 1) % len(directions) # switch direction 90 degrees to right
            next_direction = directions[dir_idx]
        
            next_i = i + next_direction[0]
            next_j = j + next_direction[1]

        transition = f'{i},{j},{next_i},{next_j}'
        if transition in transitions:
            return True
        else:
            transitions.add(transition)

        i = next_i
        j = next_j

        next_i = i + next_direction[0]
        next_j = j + next_direction[1]

    return False


def part_2(map):
    count = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '.':
                obstacle = copy.deepcopy(map)
                obstacle[i][j] = 'O'
                if contains_loop(obstacle):
                    count += 1

    return count

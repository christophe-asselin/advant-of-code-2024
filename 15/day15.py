def read_input(path):
    with open(path, 'r') as file:
        file_str = file.read()
    grid_str, moves_str = file_str.split('\n\n')

    grid = []
    for line in grid_str.split('\n'):
        grid.append(list(line.strip()))

    moves = list(moves_str.strip().replace('\n', ''))

    return grid, moves


def can_move_box(grid, box_half, direction):
    box_i, box_j_1 = box_half
    tile = grid[box_i][box_j_1]

    box_j_2 = box_j_1 + 1 if tile == '[' else box_j_1 - 1

    new_box_i = box_i + direction
    
    new_tile_1 = grid[new_box_i][box_j_1] 
    new_tile_2 = grid[new_box_i][box_j_2]

    if new_tile_1 == '#' or new_tile_2 == '#':
        return False
    if new_tile_1 == '.' and new_tile_2 == '.':
        return True

    # try moving next box/boxes
    if new_tile_1 == tile:
        return can_move_box(grid, (new_box_i, box_j_1), direction)
    else:
        res = True
        if new_tile_1 == ']' or new_tile_1 == '[':
            res = res and can_move_box(grid, (new_box_i, box_j_1), direction)
        if new_tile_2 == ']' or new_tile_2 == '[':
            res  = res and can_move_box(grid, (new_box_i, box_j_2), direction)
        return res


def try_move_box(grid, box_half, direction):
    box_i, box_j_1 = box_half
    tile = grid[box_i][box_j_1]

    box_j_2 = box_j_1 + 1 if tile == '[' else box_j_1 - 1

    new_box_i = box_i + direction
    
    new_tile_1 = grid[new_box_i][box_j_1] 
    new_tile_2 = grid[new_box_i][box_j_2]

    if new_tile_1 == '#' or new_tile_2 == '#':
        return
    if new_tile_1 == '.' and new_tile_2 == '.':
        grid[new_box_i][box_j_1] = tile 
        grid[new_box_i][box_j_2] = '[' if tile == ']' else ']'
        grid[box_i][box_j_1] = '.'
        grid[box_i][box_j_2] = '.'
        return

    # try moving next box/boxes
    if new_tile_1 == tile:
        try_move_box(grid, (new_box_i, box_j_1), direction)
    else:
        if new_tile_1 == ']' or new_tile_1 == '[':
            try_move_box(grid, (new_box_i, box_j_1), direction)
        if new_tile_2 == ']' or new_tile_2 == '[':
            try_move_box(grid, (new_box_i, box_j_2), direction)

    new_tile_1 = grid[new_box_i][box_j_1] 
    new_tile_2 = grid[new_box_i][box_j_2]

    if new_tile_1 == '.' and new_tile_2 == '.':
        grid[new_box_i][box_j_1] = tile 
        grid[new_box_i][box_j_2] = '[' if tile == ']' else ']'
        grid[box_i][box_j_1] = '.'
        grid[box_i][box_j_2] = '.'


def process_move(grid, robot, move):
    robot_i, robot_j = robot
    move_i, move_j = move

    next_robot_i, next_robot_j = robot_i + move_i, robot_j + move_j
    next_tile = grid[next_robot_i][next_robot_j]

    if next_tile == '.':
        grid[robot_i][robot_j] = '.'
        grid[next_robot_i][next_robot_j] = '@'
        return next_robot_i, next_robot_j

    if next_tile == 'O':
        next_box_i, next_box_j = next_robot_i + move_i, next_robot_j + move_j
        next_box_tile = grid[next_box_i][next_box_j]
        while next_box_tile == 'O':
            next_box_i += move_i
            next_box_j += move_j
            next_box_tile = grid[next_box_i][next_box_j]

        if next_box_tile == '.':
            grid[robot_i][robot_j] = '.'
            grid[next_robot_i][next_robot_j] = '@'
            grid[next_box_i][next_box_j] = 'O'
            return next_robot_i, next_robot_j

    if next_tile == '[' or next_tile == ']':
        if move_i == 0:  # horizontal
            next_box_i, next_box_j = next_robot_i + move_i, next_robot_j + move_j
            next_box_tile = grid[next_box_i][next_box_j]
            while next_box_tile == '[' or next_box_tile == ']':
                next_box_i += move_i
                next_box_j += move_j
                next_box_tile = grid[next_box_i][next_box_j]

            if next_box_tile == '.':
                j = next_box_j - move_j
                while grid[next_robot_i][j] != '@':
                    grid[next_robot_i][j + move_j] = grid[next_robot_i][j]
                    j -= move_j

                grid[robot_i][robot_j] = '.'
                grid[next_robot_i][next_robot_j] = '@'

                return next_robot_i, next_robot_j
        else:  # vertical
            if can_move_box(grid, (next_robot_i, next_robot_j), move_i):
                try_move_box(grid, (next_robot_i, next_robot_j), move_i)
            if grid[next_robot_i][next_robot_j] == '.':
                grid[robot_i][robot_j] = '.'
                grid[next_robot_i][next_robot_j] = '@'
                return next_robot_i, next_robot_j

    return robot


def process_moves(grid, moves):
    move_map = {
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
        'v': (1, 0)
    }

    robot = (-1, -1)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                robot = (i, j)

    for i, move in enumerate(moves):
        if move in move_map:
            #print(f'Move {move} ({i}):')
            robot = process_move(grid, robot, move_map[move])

            #for line in grid:
            #    print(''.join(line))
            #print()

    return grid


def calculate_gps_coordinates(grid, moves):
    grid = process_moves(grid, moves)
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'O' or grid[i][j] == '[':
                result += 100 * i
                result += j

    return result


def get_new_grid(grid):
    new_grid = []
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[i])):
            tile = grid[i][j]
            if tile == '#':
                new_row.append('#')
                new_row.append('#')
            elif tile == 'O':
                new_row.append('[')
                new_row.append(']')
            elif tile == '.':
                new_row.append('.')
                new_row.append('.')
            else:  # @
                new_row.append('@')
                new_row.append('.')
        new_grid.append(new_row)
    return new_grid

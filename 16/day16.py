from collections import defaultdict
import heapq


def read_input(path):
    with open(path, 'r') as file:
        return [[tile for tile in list(line.strip())] for line in file]

def get_start_end(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'S':
                start = (i, j)
            if map[i][j] == 'E':
                end = (i, j)
    return start, end


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(map, start, end):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]
    default_direction = (0, 1)
    min_heap = []
    heapq.heappush(min_heap, (manhattan(start, end), (start, default_direction)))
    print(min_heap)

    came_from = {}

    g_score = defaultdict(lambda: float('inf'))
    g_score[start] = 0

    f_score = defaultdict(lambda: float('inf'))
    f_score[start] = manhattan(start, end)

    while len(min_heap) > 0:
        _, (current, current_direction) = heapq.heappop(min_heap)
        curr_i, curr_j = current

        if current == end:
            return g_score[current], came_from

        for direction in directions:
            curr_i, curr_j = current
            curr_dir_i, curr_dir_j = current_direction
            dir_i, dir_j = direction

            neighbor = (curr_i + dir_i, curr_j + dir_j)
            neighbor_i, neighbor_j = neighbor

            if map[neighbor_i][neighbor_j] == '#':
                continue

            if direction == current_direction:
                weight = 1
            elif curr_dir_i == dir_i or curr_dir_j == dir_j:
                weight = 2001 # turn 180 degrees and move one
            else:
                weight = 1001 # turn 90 degrees and move one

            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = (current, direction)
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + manhattan(neighbor, end)
                
                if (neighbor, direction) not in min_heap:
                    heapq.heappush(min_heap, (f_score[neighbor], (neighbor, direction)))


def print_path(map, came_from, current):
    while current in came_from:
        current, direction = came_from[current]
        if direction == (0, 1):
            map[current[0]][current[1]] = '>'
        elif direction == (0, -1):
            map[current[0]][current[1]] = '<'
        elif direction == (1, 0):
            map[current[0]][current[1]] = 'v'
        else:
            map[current[0]][current[1]] = '^'
    print()
    for row in map:
        print(''.join(row))

        
def cheapest_cost(map):
    start, end = get_start_end(map)
    cost, came_from = a_star(map, start, end)
    # print_path(map, came_from, end)
    return cost

    


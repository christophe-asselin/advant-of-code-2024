import re


def read_input(path):
    robots = []
    
    with open(path, 'r') as file:
        for line in file:
            regex = r'p=([0-9]+),([0-9]+) v=(\-?[0-9]+),(\-?[0-9]+)'
            match = re.match(regex, line).groups()
            p_x = int(match[0])
            p_y = int(match[1])
            v_x = int(match[2])
            v_y = int(match[3])

            robots.append(((p_x, p_y), (v_x, v_y)))

    return robots


def positions_after_seconds(robots, width, height, seconds):
    positions = []
    for (p_x, p_y), (v_x, v_y) in robots:
        final_p_x = (p_x + (v_x * seconds)) % width
        final_p_y = (p_y + (v_y * seconds)) % height
        positions.append((final_p_x, final_p_y))

    return positions


def safety_score(robots, width, height, seconds):
    positions = positions_after_seconds(robots, width, height, seconds)
    q1, q2, q3, q4 = 0, 0, 0, 0
    mid_height = height // 2
    mid_width = width // 2
    for x, y in positions:
        if 0 <= x < mid_width and 0 <= y < mid_height:
            q1 += 1
        elif mid_width < x < width and 0 <= y < mid_height:
            q2 += 1
        elif 0 <= x < mid_width and mid_height < y < height:
            q3 += 1
        elif mid_width < x < width and mid_height < y < height:
            q4 += 1
        else:
            pass

    return q1 * q2 * q3 * q4


def pretty_print_robots(positions, width, height):
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for x, y in positions:
        grid[y][x] = '#'
    print()
    for row in grid:
        print(''.join(row))
    print()



def iterate_through(robots, width, height):
    scores = []
    for i in range(10_000):
        scores.append(safety_score(robots, width, height, i))
    min_score = min(scores)
    res = scores.index(min_score)
    pretty_print_robots(positions_after_seconds(robots, width, height, res), width, height)
    return res

    
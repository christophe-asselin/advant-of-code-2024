def read_input(path):
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file]
    

def is_in_plot(map, i, j, plot_value):
    return i >= 0 and i < len(map) and j >= 0 and j < len(map[i]) and map[i][j] == plot_value


def get_plot(map, i, j):
    plot = set()
    perimeter = 0
    stack = [(i, j)]
    plot_value = map[i][j]
    while len(stack) > 0:
        curr = stack.pop()
        curr_i, curr_j = curr
        if curr not in plot:
            if is_in_plot(map, curr_i, curr_j, plot_value):
                plot.add(curr)
                stack.append((curr_i + 1, curr_j))
                stack.append((curr_i - 1, curr_j))
                stack.append((curr_i, curr_j + 1))
                stack.append((curr_i, curr_j - 1))
            else:
                perimeter += 1

    return plot, perimeter


def calculate_fence_price(map):
    visited = set()
    cost = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i, j) not in visited:
                plot, perimeter = get_plot(map, i, j)
                visited.update(plot)
                cost += len(plot) * perimeter
    return cost


def get_n_corners(i, j, plot):
    corners = 0
    # convex
    if (i - 1, j) not in plot and (i, j - 1) not in plot:
        corners += 1

    if (i - 1, j) not in plot and (i, j + 1) not in plot:
        corners += 1

    if (i + 1, j) not in plot and (i, j - 1) not in plot:
        corners += 1

    if (i + 1, j) not in plot and (i, j + 1) not in plot:
        corners += 1

    # concave
    if (i - 1, j) in plot and (i - 1, j - 1) not in plot and (i, j - 1) in plot:
        corners += 1

    if (i - 1, j) in plot and (i - 1, j + 1) not in plot and (i, j + 1) in plot:
        corners += 1

    if (i + 1, j) in plot and (i + 1, j - 1) not in plot and (i, j - 1) in plot:
        corners += 1

    if (i + 1, j) in plot and (i + 1, j + 1) not in plot and (i, j + 1) in plot:
        corners += 1

    return corners


def get_plot_with_sides(map, i, j):
    plot = set()
    stack = [(i, j)]
    plot_value = map[i][j]
    while len(stack) > 0:
        curr = stack.pop()
        curr_i, curr_j = curr
        if curr not in plot:
            if is_in_plot(map, curr_i, curr_j, plot_value):
                plot.add(curr)
                stack.append((curr_i + 1, curr_j))
                stack.append((curr_i - 1, curr_j))
                stack.append((curr_i, curr_j + 1))
                stack.append((curr_i, curr_j - 1))

    sides = sum([get_n_corners(i, j, plot) for i, j in plot])

    return plot, sides


def calculate_side_price(map):
    visited = set()
    cost = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i, j) not in visited:
                plot, perimeter = get_plot_with_sides(map, i, j)
                visited.update(plot)
                cost += len(plot) * perimeter
    
    return cost
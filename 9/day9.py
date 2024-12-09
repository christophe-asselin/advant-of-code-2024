
empty = '.'

def read_input(path):
    with open(path, 'r') as file:
        disk_map_str = file.read()
    return [int(x) for x in list(disk_map_str)]


def expand_disk_map(disk_map):
    id = 0
    disk_map_list = []
    for i, element in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(element):
                disk_map_list.append(id)
            id += 1
        else:
            for _ in range(element):
                disk_map_list.append(empty)

    return disk_map_list
    

def reorder_blocks(disk_map):
    l = 0
    r = len(disk_map) - 1
    while l < r:
        if disk_map[l] != empty:
            l += 1
        if disk_map[r] == empty:
            r -= 1

        if disk_map[l] == empty and disk_map[r] != empty:
            disk_map[l], disk_map[r] = disk_map[r], disk_map[l]
            l += 1
            r -= 1
    
    return disk_map


def calculate_checksum(disk_map):
    result = 0
    for i, id in enumerate(disk_map):
        if id != '.':
            result += i * id
    return result


def part_1(path):
    raw_disk_map = read_input(path)
    expanded_disk_map = expand_disk_map(raw_disk_map)
    compressed_disk_map = reorder_blocks(expanded_disk_map)
    return calculate_checksum(compressed_disk_map)


def get_end(disk_map, start, reversed):
    i = start
    id = disk_map[i]
    while i >= 0 and i < len(disk_map) and disk_map[i] == id:
        if reversed:
            i -= 1
        else:
            i += 1
    return i


def swap_files(disk_map):
    l = 0
    r = len(disk_map) - 1
    while l < r:
        while disk_map[l] != empty: # find next empty space
            l += 1
        while disk_map[r] == empty: # find next file
            r -= 1

        free_end = get_end(disk_map, l, False)
        free_size = free_end - l
        file_end = get_end(disk_map, r, True)
        file_size = r - file_end

        if l >= r: # move to next file if no empty space to the left
            l = 0
            r = file_end
        elif free_size >= file_size: # fits in empty space
            for _ in range(file_size):
                disk_map[l], disk_map[r] = disk_map[r], disk_map[l]
                l += 1
                r -= 1
            l = 0
            r = file_end
        else: # move on the next free space
            l = free_end


    return disk_map
    
def part_2(path):
    raw_disk_map = read_input(path)
    expanded = expand_disk_map(raw_disk_map)
    compressed = swap_files(expanded)
    return calculate_checksum(compressed)

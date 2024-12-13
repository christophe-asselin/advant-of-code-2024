from day9 import *


def test_read_input():
    actual = read_input('./09/test_input.txt')
    expected = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
    assert actual == expected


def test_expand_disk_map():
    disk_map = [2, 3, 3, 3, 1, 3, 3, 1, 2, 1, 4, 1, 4, 1, 3, 1, 4, 0, 2]
    expected = [0, 0, empty, empty, empty, 1, 1, 1, empty, empty, empty, 2, empty, empty, empty, 3, 3, 3, empty, 4, 4, empty, 5, 5, 5, 5, empty, 6, 6, 6, 6, empty, 7, 7, 7, empty, 8, 8, 8, 8, 9, 9]
    actual = expand_disk_map(disk_map)
    assert actual == expected


def test_reorder_blocks():
    disk_map = [0, 0, empty, empty, empty, 1, 1, 1, empty, empty, empty, 2, empty, empty, empty, 3, 3, 3, empty, 4, 4, empty, 5, 5, 5, 5, empty, 6, 6, 6, 6, empty, 7, 7, 7, empty, 8, 8, 8, 8, 9, 9]
    expected = '0099811188827773336446555566..............'
    actual = ''.join([str(x) for x in reorder_blocks(disk_map)])
    assert actual == expected


def test_calculate_checksum():
    disk_map = [int(x) if x.isdigit() else x for x in list('0099811188827773336446555566..............')]
    expected = 1928
    actual = calculate_checksum(disk_map)
    assert actual == expected


def test_part_1():
    expected = 1928
    actual = part_1('./09/test_input.txt')
    assert actual == expected


def test_get_end():
    disk_map = [0, 0, '.', '.', 1, 1, '.', '.']
    l = 2
    free_end = get_end(disk_map, l, reversed=False)
    expected = 4
    assert free_end == expected

    r = 5
    file_end = get_end(disk_map, r, reversed=True)
    expected = 3
    assert file_end == expected


def test_swap_files():
    disk_map = [0, 0, '.', '.', 1, 1, '.', '.']
    actual = swap_files(disk_map)
    expected = [0, 0, 1, 1, '.', '.', '.', '.']
    assert actual == expected


def test_part_2():
    actual = part_2('./09/test_input.txt')
    expected = 2858
    assert actual == expected
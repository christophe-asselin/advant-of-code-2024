from day4 import *


def test_part_1():
    input = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
    expected = 18
    assert part_1(input) == expected
    print("test_matches_part_1 passed")


def test_matches_matrix():
    input = [
        ['M', 'A', 'S'],
        ['T', 'A', 'B'],
        ['M', 'P', 'S']
    ]
    xmas_matrix = [
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S']
    ]
    assert matches_matrix(input, 0, 0, xmas_matrix) == True
    print("test_matches_matrix passed")


def test_part_2():
    input = '''.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
'''
    expected = 9
    actual = part_2(input)
    assert actual == expected
    print("test_matches_part_2 passed")


if __name__ == '__main__':
    test_part_1()
    test_matches_matrix()
    test_part_2()
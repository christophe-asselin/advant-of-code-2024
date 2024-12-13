from collections import defaultdict


def read_input():
    list_a = []
    list_b = []
    path = '.\\1\\input.txt'
    with open(path, 'r') as file:
        for line in file:
            parts = line.split()
            list_a.append(int(parts[0]))
            list_b.append(int(parts[1]))
    return list_a, list_b


def part_1(list_a, list_b):
    sorted_list_a = sorted(list_a)
    sorted_list_b = sorted(list_b)

    total_distance = 0
    for i, a in enumerate(sorted_list_a):
        b = sorted_list_b[i]
        total_distance += abs(a - b)

    print('part 1: {}'.format(total_distance))


def part_2(list_a, list_b):
    occurences = defaultdict(int)
    for b in list_b:
        occurences[b] += 1

    similarity_score = 0
    for a in list_a:
        similarity_score += a * occurences[a]

    print('part 2: {}'.format(similarity_score))


def main():
    list_a, list_b = read_input()
    part_1(list_a, list_b)
    part_2(list_a, list_b)


if __name__ == '__main__':
    main()

def read_input():
    with open('./02/input.txt', 'r') as file:
        return [[int(level) for level in line.split()] for line in file]


def part_1(reports):
    safe_count = 0
    
    for report in reports:
        is_increasing = report[0] < report[1]
        is_safe = 1
        for i in range(len(report) - 1):
            if is_increasing:
                if not (report[i] + 1 <= report[i + 1] <= report[i] + 3):
                    is_safe = 0
                    break
            else:
                if not (report[i] - 1 >= report[i + 1] >= report[i] - 3):
                    is_safe = 0
                    break

        safe_count += is_safe

    print(safe_count)


def get_variations(report):
    return [[level for j, level in enumerate(report) if i != j] for i in range(-1, len(report))]


def check_is_safe(report):
    is_increasing = report[0] < report[1]
    for i in range(len(report) - 1):
        if is_increasing:
            if not (report[i] + 1 <= report[i + 1] <= report[i] + 3):
                return False
        else:
            if not (report[i] - 1 >= report[i + 1] >= report[i] - 3):
                return False
    return True


def part_2(reports):
    safe_count = 0
    
    for report in reports:
        report_variations = get_variations(report)
        for variation in report_variations:
            if check_is_safe(variation):
                safe_count += 1
                break

    print(safe_count)


def main():
    reports = read_input()
    part_1(reports)
    part_2(reports)


if __name__ == '__main__':
    main()
import re


def read_input():
    with open('./3/input.txt', 'r') as file:
        return ''.join(file)


def part_1(text):
    matches = re.findall(r'mul\(([0-9]+),([0-9]+)\)', text)
    products = [int(pair[0]) * int(pair[1]) for pair in matches]
    return sum(products)


def test_part_1():
    text = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    expected = 161
    assert part_1(text) == expected


def part_2(text):
    matches = re.findall(r"(do\(\))|(don't\(\))|mul\(([0-9]+),([0-9]+)\)", text)
    
    enabled = True
    result = 0

    for match in matches:
        if match[0]: # do() matched
            enabled = True
        elif match[1]: # don't() matched
            enabled = False
        elif match[2] and match[3] and enabled:
            result += int(match[2]) * int(match[3])
        else:
            pass

    return result


def test_part_2():
    text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    expected = 48
    assert part_2(text) == expected


def main():
    test_part_1()
    test_part_2()

    input = read_input()
    print('Part 1: {}'.format(part_1(input)))
    print('Part 2: {}'.format(part_2(input)))


if __name__ == '__main__':
    main()
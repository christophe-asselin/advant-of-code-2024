from collections import namedtuple


Equation = namedtuple('Equation', ['test_value', 'numbers'])


def read_input(path):
    equations = []
    with open(path, 'r') as file:
        for line in file:
            parts = line.split(':')
            test_value = int(parts[0])
            numbers = [int(number) for number in parts[1].split()]
            equations.append(Equation(test_value=test_value, numbers=numbers))

    return equations


def is_valid(equation, operator):
    test_value, numbers = equation
    if len(numbers) == 1:
        return test_value == numbers[0]
    
    a, b = numbers[:2]
    result = None
    if operator == '+':
        result = a + b
    else:
        result = a * b

    if result > test_value: # value will only get larger
        return False
    
    new_equation = Equation(test_value=test_value, numbers=[result, *numbers[2:]])

    return is_valid(new_equation, '+') or is_valid(new_equation, '*')



def part_1(equations):
    result = 0
    for equation in equations:
        if is_valid(equation, '+') or is_valid(equation, '*'):
            result += equation.test_value

    return result


def is_valid_2(equation, operator):
    test_value, numbers = equation
    if len(numbers) == 1:
        return test_value == numbers[0]
    
    a, b = numbers[:2]
    result = None
    if operator == '+':
        result = a + b
    elif operator == '*':
        result = a * b
    else:
        result = int(str(a) + str(b))

    if result > test_value: # value will only get larger
        return False
    
    new_equation = Equation(test_value=test_value, numbers=[result, *numbers[2:]])

    return is_valid_2(new_equation, '+') or is_valid_2(new_equation, '*') or is_valid_2(new_equation, '||')


def part_2(equations):
    result = 0
    for equation in equations:
        if is_valid_2(equation, '+') or is_valid_2(equation, '*') or is_valid_2(equation, '||'):
            result += equation.test_value

    return result

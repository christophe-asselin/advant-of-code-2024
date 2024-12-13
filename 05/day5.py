from collections import defaultdict
from functools import cmp_to_key

def read_input():
    with open('./05/input.txt', 'r') as file:
        text_file =  file.read()
    return text_file.split('\n\n')


def format_input(rules, updates):
    rules = [[int(n) for n in rule.split('|')] for rule in rules.split('\n')]
    updates = [[int(n) for n in update.split(',')] for update in updates.split('\n')]

    rules_dict = defaultdict(set)

    for rule in rules:
        a, b = rule
        if a not in rules_dict:
            rules_dict[a] = set([b])
        else:
            rules_dict[a].add(b)


    return rules_dict, updates


def part_1(rules, updates):
    rules, updates = format_input(rules, updates)
    result = 0

    for update in updates:
        is_correct = True
        seen_so_far = set()
        for page in update:
            forbidden = rules[page]
            if (seen_so_far & forbidden):
                is_correct = False
                break
            seen_so_far.add(page)

        if is_correct:
            result += update[len(update) // 2]
    
    return result


def part_2(rules, updates):
    rules, updates = format_input(rules, updates)
    result = 0

    for update in updates:
        is_correct = True
        seen_so_far = set()
        for page in update:
            forbidden = rules[page]
            if (seen_so_far & forbidden):
                is_correct = False
                break
            seen_so_far.add(page)

        if not is_correct:
            update = sorted(update, key=cmp_to_key(lambda a, b: 1 if b in rules[a] else -1)) 
            result += update[len(update) // 2]
    
    return result
            
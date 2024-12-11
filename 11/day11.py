def read_input(path):
    with open(path, 'r') as file:
        return [int(n) for n in file.read().split()]


def recursive_blink(stone, depth, max_depth, cache):
    if depth == max_depth:
        return 1

    cache_key = f'{stone, depth}'
    if cache_key in cache:
        return cache[cache_key]

    if stone == 0:
        res = recursive_blink(1, depth + 1, max_depth, cache)
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        a = int(stone_str[:len(stone_str) // 2])
        b = int(stone_str[len(stone_str) // 2:])
        res = recursive_blink(a, depth + 1, max_depth, cache) + \
            recursive_blink(b, depth + 1, max_depth, cache)
    else:
        res = recursive_blink(stone * 2024, depth + 1, max_depth, cache)

    cache[cache_key] = res
    return res


def count_after_blinks_recursive(stones, n):
    result = 0
    cache = {}
    for stone in stones:
        result += recursive_blink(stone, 0, n, cache)
    return result


def count_after_blinks(stones, n):
    for j in range(n):
        for i in range(len(stones)):
            stone_str = str(stones[i])
            if stones[i] == 0:
                stones[i] = 1
            elif len(stone_str) % 2 == 0:
                stones[i] = int(stone_str[:len(stone_str) // 2])
                stones.append(int(stone_str[len(stone_str) // 2:]))
            else:
                stones[i] *= 2024
    return len(stones)

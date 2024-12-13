import numpy as np
from collections import defaultdict

line = open("data/11.out", "r").read()

stones = list(map(int, line.strip().split()))

def handle_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_string = str(stone)
        return [int(stone_string[:len(stone_string)//2]), int(stone_string[len(stone_string)//2:])]
    else:
        return [stone * 2024]
    
def blink(stones_map):
    new_stones_map = defaultdict(int)
    for stone, count in stones_map.items():
        new_stones = handle_stone(stone)
        for new_stone in new_stones:
            new_stones_map[new_stone] += count
    return new_stones_map

def flatten(lst):
    return [item for sublist in lst for item in (sublist if isinstance(sublist, list) else [sublist])]

part_1 = 0

stones_map = defaultdict(int)
for stone in stones:
    stones_map[stone] += 1
for _ in range(75):
    stones_map = blink(stones_map)

# part_1 += len(stones)

print('Part 1:', sum(list(stones_map.values())))
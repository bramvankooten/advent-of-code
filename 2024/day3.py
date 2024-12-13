import re

lines = open("data/3.out", "r").readlines()

lines = [line.strip() for line in lines]

part_1 = 0

for line in lines:
    part_1 += sum([int(x[0]) * int (x[1]) for x in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)])

print('Part 1:', part_1)

part_2 = 0

enabled = True

for line in lines:
    partitioned = [re.split(r"(don't\(\))", part) for part in re.split(r'(do\(\))', line)]
    partitioned = [x for xs in partitioned for x in xs]

    for part in partitioned:
        if part == "don't()":
            enabled = False
        elif part == 'do()':
            enabled = True
        elif enabled:
            part_2 += sum([int(x[0]) * int (x[1]) for x in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', part)])

print("Part 2:",part_2)
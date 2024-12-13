import math

lines = open("data/5.out", "r").readlines()

lines = [line.strip() for line in lines]

before = dict()
after = dict()

line = lines.pop(0)
while line:
    pages = line.split('|')

    if pages[0] in after:
        after[pages[0]].append(pages[1])
    else:
        after[pages[0]] = [pages[1]]

    if pages[1] in before:
        before[pages[1]].append(pages[0])
    else:
        before[pages[1]] = [pages[0]]
    line = lines.pop(0)

updates = [line.strip().split(',') for line in lines]

def inner(u):
    for i in range(len(u)):
        if any(p in after.get(u[i], []) for p in u[:i]) or any(p in before.get(u[i], []) for p in u[i:]):
            return False
    return True

correct_updates = []
incorrect_updates = []

for u in updates:
    if inner(u):
        correct_updates.append(u)
    else:
        incorrect_updates.append(u)

part_1 = 0

for c in correct_updates:
    part_1 += int(c[math.floor(len(c)/2)])

print('Part 1:', part_1)

fixed_updates = []

for inc in incorrect_updates:
    reorder = [inc[0]]
    
    for i in range(1, len(inc)):
        added = False
        for j in range(len(reorder)):
            if reorder[j] in after.get(inc[i], []) and not added:
                reorder.insert(j, inc[i])
                added = True
        if not added:
            reorder.append(inc[i])
    fixed_updates.append(reorder)

part_2 = 0

for f in fixed_updates:
    part_2 += int(f[math.floor(len(f)/2)])

print('Part 2:', part_2)

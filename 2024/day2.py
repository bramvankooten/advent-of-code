lines = open("data/2.out", "r").readlines()

lines = [list(map(int, line.strip().split(' '))) for line in lines]

def inner(line):
    dif = line[0] - line[1]
    if dif == 0 or abs(dif) > 3:
        return 0
    for i in range(1, len(line)-1):
        new_dif = line[i] - line[i+1]
        if new_dif == 0 or abs(new_dif) > 3 or dif*new_dif < 0:
            return 0
        else:
            dif = new_dif
    
    return 1

part_1 = 0

for line in lines:
    part_1 += inner(line)

print('Part 1:', part_1)

part_2 = 0

def check(line):
    if inner(line):
        return 1
    
    for i in range(len(line)):
        part = line[:i] + line[i+1:]
        if inner(part):
            return 1
        
    return 0

for line in lines:
    part_2 += check(line)

print('Part 2:', part_2)
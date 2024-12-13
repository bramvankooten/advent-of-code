import numpy as np

lines = open("data/8.out", "r").readlines()

lines = np.array([np.array(list(line.strip())) for line in lines])

freq = [str(x) for x in np.unique(lines) if x != '.']

towers = []

for f in freq:
    loc = np.argwhere(lines == f)
    for i in range(len(loc)-1):
        for j in range(i+1, len(loc)):
            dif = loc[i] - loc[j]
            towers.append(loc[i] - dif*-1)
            towers.append(loc[j] - dif)


tower_map = lines.copy()

for t in towers:
    if all(t < lines.shape) and all(t >= [0,0]):
        tower_map[t[0],t[1]] = '#'

print('Part 1:', len(np.argwhere(tower_map == '#')))

towers = []

for f in freq:
    loc = np.argwhere(lines == f)
    for i in range(len(loc)-1):
        for j in range(i+1, len(loc)):
            dif = loc[i] - loc[j]
            for n in range(lines.shape[0]+1):
                towers.append(loc[i] - dif*-n)
                towers.append(loc[j] - dif*n)

tower_map = lines.copy()

for t in towers:
    if all(t < lines.shape) and all(t >= [0,0]):
        tower_map[t[0],t[1]] = '#'

print('Part 2:', len(np.argwhere(tower_map == '#')))

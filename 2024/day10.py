import numpy as np

lines = open("data/10.test", "r").readlines()

lines = np.array([list(map(int, np.array(list(line.strip())))) for line in lines])

def within_bounds(coord):
    return all(coord < lines.shape) and all(coord >= [0,0])

def get_neighbors(coord, height):
    neighbors = []
    up = coord + np.array([-1,0])
    if within_bounds(up) and lines[up[0],up[1]] == height + 1:
        neighbors.append(up)

    down = coord + np.array([1,0])
    if within_bounds(down) and lines[down[0],down[1]] == height + 1:
        neighbors.append(down)

    left = coord + np.array([0,-1])
    if within_bounds(left) and lines[left[0],left[1]] == height + 1:
        neighbors.append(left)

    right = coord + np.array([0,1])
    if within_bounds(right) and lines[right[0],right[1]] == height + 1:
        neighbors.append(right)

    return neighbors
    
zeros = np.argwhere(lines == 0)

part_1 = 0
part_2 = 0

for z in zeros:
    options = [z]

    for i in range(9):
        new_options = []
        for o in options:
            new_options.extend(get_neighbors(o, lines[o[0],o[1]]))
        options = new_options
    
    part_1 += len(np.unique(options, axis=0))
    part_2 += len(options)

print('Part 1:', part_1)
print('Part 2:', part_2)

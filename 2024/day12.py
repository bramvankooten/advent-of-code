import numpy as np

lines = open("data/12.out", "r").readlines()

lines = np.array([np.array(list(line.strip())) for line in lines])
lines = np.insert(lines, len(lines), '.', axis=0)
lines = np.insert(lines, 0, '.', axis=0)
lines = np.insert(lines, len(lines[0]), '.', axis=1)
lines = np.insert(lines, 0, '.', axis=1)
print(lines)

plant_types = [str(x) for x in np.unique(lines) if x != '.']

def add_tuple(first, second):
    return tuple(a + b for a, b in zip(first, second))

def get_neighbors(coord):
    char = lines[coord]
    up = add_tuple(coord, (-1,0))
    down = add_tuple(coord, (1,0))
    left = add_tuple(coord, (0,-1))
    right = add_tuple(coord, (0,1))

    new_coords = [x for x in [up, down, left, right] if lines[x] == char]
    return new_coords, 4-len(new_coords)


def get_neigborhood(coord):
    to_check = set([coord])
    visited = set()
    total_perimiter = 0 

    
    while to_check:
        current = to_check.pop()
        visited.add(current)
        new_coords, perimiter = get_neighbors(current)
        for n in new_coords:
            if n not in visited:
                to_check.add(n)
        total_perimiter += perimiter
    
    return visited, total_perimiter

def get_sides(coords):
    sides = 0
    for x in range(len(lines[0])):
        left_sides = 0
        checking_side = False
        for y in range(len(lines)):
            if (y,x) in coords and not checking_side:
                if add_tuple((y,x), (0,-1)) not in coords:
                    checking_side = True
            elif (y,x) in coords:
                if add_tuple((y,x), (0,-1)) in coords:
                    checking_side = False
                    left_sides += 1
            elif (y,x) not in coords and checking_side:
                checking_side = False
                left_sides += 1
            else:
                pass
        sides += left_sides

        right_sides = 0
        checking_side = False
        for y in range(len(lines)):
            if (y,x) in coords and not checking_side:
                if add_tuple((y,x), (0,1)) not in coords:
                    checking_side = True
            elif (y,x) in coords:
                if add_tuple((y,x), (0,1)) in coords:
                    checking_side = False
                    right_sides += 1
            elif (y,x) not in coords and checking_side:
                checking_side = False
                right_sides += 1
            else:
                pass
        sides += right_sides

    for y in range(len(lines)):
        up_sides = 0
        checking_side = False
        for x in range(len(lines[0])):
            if (y,x) in coords and not checking_side:
                if add_tuple((y,x), (-1,0)) not in coords:
                    checking_side = True
            elif (y,x) in coords:
                if add_tuple((y,x), (-1,0)) in coords:
                    checking_side = False
                    up_sides += 1
            elif (y,x) not in coords and checking_side:
                checking_side = False
                up_sides += 1
            else:
                pass
        sides += up_sides

        down_sides = 0
        checking_side = False
        for x in range(len(lines[0])):
            if (y,x) in coords and not checking_side:
                if add_tuple((y,x), (1,0)) not in coords:
                    checking_side = True
            elif (y,x) in coords:
                if add_tuple((y,x), (1,0)) in coords:
                    checking_side = False
                    down_sides += 1
            elif (y,x) not in coords and checking_side:
                checking_side = False
                down_sides += 1
            else:
                pass
        sides += down_sides

    return sides

part_1 = 0
part_2 = 0

for p in plant_types:
    locations = np.where(lines == p)

    while locations[0].size > 0:
        coord = (locations[0][0], locations[1][0])
        neighborhood, perim = get_neigborhood(coord)
        sides = get_sides(neighborhood)
        for n in neighborhood:
            lines[n] = '.'

        part_1 += (len(neighborhood) * perim)
        part_2 += (len(neighborhood) * sides)
        locations = np.where(lines == p)


print('Part 1:', part_1)
print('Part 2:', part_2)
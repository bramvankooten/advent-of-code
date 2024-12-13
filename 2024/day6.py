import numpy as np
from enum import Enum

lines = open("data/6.out", "r").readlines()

lines = np.array([np.array(list(line.strip())) for line in lines])

walls = np.argwhere(lines == '#')
start_point = np.argwhere(lines == '^')
current_location = start_point[0]

print(current_location)

Direction = Enum('Direction', 'UP DOWN LEFT RIGHT')

dir = Direction.UP

print(lines)

done = False

while not done:
    if dir == Direction.UP:
        cur_x = current_location[1]
        
        line_walls = [w for w in walls if w[1] == cur_x]
        wall_y = float('-inf')
        for w in line_walls:
            if w[0] > wall_y and w[0] < current_location[0]:
                wall_y = w[0]

        if wall_y < 0:
            done = True
            lines[0:current_location[0], cur_x] = 'X'
        else:
            lines[wall_y+1:current_location[0]+1, cur_x] = 'X'
            current_location = [wall_y+1, cur_x]
            dir = Direction.RIGHT
    elif dir == Direction.RIGHT:
        cur_y = current_location[0]
        

        line_walls = [w for w in walls if w[0] == cur_y]
        wall_x = float('inf')
        for w in line_walls:
            if w[1] < wall_x and w[1] > current_location[1]:
                wall_x = w[1]
        if wall_x > len(lines[0]):
            done = True
            lines[cur_y, current_location[1]:len(lines[0])] = 'X'
        else:
            lines[cur_y, current_location[1]:wall_x] = 'X'
            current_location = [cur_y, wall_x-1]
            dir = Direction.DOWN
    elif dir == Direction.DOWN:
        cur_x = current_location[1]
        
        line_walls = [w for w in walls if w[1] == cur_x]
        wall_y = float('inf')
        for w in line_walls:
            if w[0] < wall_y and w[0] > current_location[0]:
                wall_y = w[0]

        if wall_y > len(lines):
            done = True
            lines[current_location[0]:len(lines), cur_x] = 'X'
        else:
            lines[current_location[0]:wall_y, cur_x] = 'X'
            current_location = [wall_y-1, cur_x]
            dir = Direction.LEFT
    elif dir == Direction.LEFT:
        cur_y = current_location[0]

        line_walls = [w for w in walls if w[0] == cur_y]
        wall_x = float('-inf')
        for w in line_walls:
            if w[1] > wall_x and w[1] < current_location[1]:
                wall_x = w[1]

        if wall_x < 0 :
            done = True
            lines[cur_y, 0:current_location[1]] = 'X'
        else:
            lines[cur_y, wall_x+1:current_location[1]] = 'X'
            current_location = [cur_y, wall_x+1]
            dir = Direction.UP
print(lines)

print('Part 1:', len(np.argwhere(lines == 'X')))
import numpy as np

lines = open("data/4.out", "r").readlines()

lines = np.array([np.array(list(line.strip())) for line in lines])

part_1 = 0

for y in range(len(lines)):
    for x in range(len(lines[0])):
        char = lines[y][x]
        if char == 'X':
            if y < 3 and x < 3:
                part_1 += 1 if lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y][x+3] == 'XMAS' else 0 # right
                part_1 += 1 if lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == 'XMAS' else 0 # down right
                part_1 += 1 if lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == 'XMAS' else 0 # down
            elif y >= len(lines)-3 and x >= len(lines[0])-3:
                part_1 += 1 if lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3] == 'XMAS' else 0 # left
                part_1 += 1 if lines[y][x] + lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == 'XMAS' else 0 # top left
                part_1 += 1 if lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == 'XMAS' else 0 # top
            elif y < 3 and x >= len(lines[0])-3:
                part_1 += 1 if lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == 'XMAS' else 0 # down
                part_1 += 1 if lines[y][x] + lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == 'XMAS' else 0 # down left
                part_1 += 1 if lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3] == 'XMAS' else 0 # left
            elif y >= len(lines)-3 and x < 3:
                part_1 += 1 if lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == 'XMAS' else 0 # top
                part_1 += 1 if lines[y][x] + lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == 'XMAS' else 0 # top right
                part_1 += 1 if lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y][x+3] == 'XMAS' else 0 # right
            elif y < 3:
                part_1 += 1 if lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y][x+3] == 'XMAS' else 0 # right
                part_1 += 1 if lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == 'XMAS' else 0 # down right
                part_1 += 1 if lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == 'XMAS' else 0 # down
                part_1 += 1 if lines[y][x] + lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == 'XMAS' else 0 # down left
                part_1 += 1 if lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3] == 'XMAS' else 0 # left
            elif y >= len(lines)-3:
                part_1 += 1 if lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3] == 'XMAS' else 0 # left
                part_1 += 1 if lines[y][x] + lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == 'XMAS' else 0 # top left
                part_1 += 1 if lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == 'XMAS' else 0 # top
                part_1 += 1 if lines[y][x] + lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == 'XMAS' else 0 # top right
                part_1 += 1 if lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y][x+3] == 'XMAS' else 0 # right
            elif x < 3:
                part_1 += 1 if lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == 'XMAS' else 0 # top
                part_1 += 1 if lines[y][x] + lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == 'XMAS' else 0 # top right
                part_1 += 1 if lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y][x+3] == 'XMAS' else 0 # right
                part_1 += 1 if lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == 'XMAS' else 0 # down right
                part_1 += 1 if lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == 'XMAS' else 0 # down
            elif x >= len(lines[0])-3:
                part_1 += 1 if lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == 'XMAS' else 0 # down
                part_1 += 1 if lines[y][x] + lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == 'XMAS' else 0 # down left
                part_1 += 1 if lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3] == 'XMAS' else 0 # left
                part_1 += 1 if lines[y][x] + lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == 'XMAS' else 0 # top left
                part_1 += 1 if lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == 'XMAS' else 0 # top
            else:
                part_1 += 1 if lines[y][x] + lines[y][x+1] + lines[y][x+2] + lines[y][x+3] == 'XMAS' else 0 # right
                part_1 += 1 if lines[y][x] + lines[y+1][x+1] + lines[y+2][x+2] + lines[y+3][x+3] == 'XMAS' else 0 # down right
                part_1 += 1 if lines[y][x] + lines[y+1][x] + lines[y+2][x] + lines[y+3][x] == 'XMAS' else 0 # down
                part_1 += 1 if lines[y][x] + lines[y+1][x-1] + lines[y+2][x-2] + lines[y+3][x-3] == 'XMAS' else 0 # down left
                part_1 += 1 if lines[y][x] + lines[y][x-1] + lines[y][x-2] + lines[y][x-3] == 'XMAS' else 0 # left
                part_1 += 1 if lines[y][x] + lines[y-1][x-1] + lines[y-2][x-2] + lines[y-3][x-3] == 'XMAS' else 0 # top left
                part_1 += 1 if lines[y][x] + lines[y-1][x] + lines[y-2][x] + lines[y-3][x] == 'XMAS' else 0 # top
                part_1 += 1 if lines[y][x] + lines[y-1][x+1] + lines[y-2][x+2] + lines[y-3][x+3] == 'XMAS' else 0 # top right

print('Part 1:', part_1)

part_2 = 0

for y in range(len(lines)-2):
    for x in range(len(lines[0])-2):
        part = lines[y:y+3, x:x+3]
        part_2 += 1 if (lines[y,x] + lines[y+1, x+1] + lines[y+2, x+2] == 'MAS' or lines[y,x] + lines[y+1, x+1] + lines[y+2, x+2] == 'SAM') and (lines[y+2,x] + lines[y+1, x+1] + lines[y, x+2] == 'MAS' or lines[y+2,x] + lines[y+1, x+1] + lines[y, x+2] == 'SAM') else 0

print('Part 2:', part_2)
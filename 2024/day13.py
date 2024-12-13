import re
import numpy as np
from itertools import product
import math

lines = open("data/13.test", "r").readlines()

lines = [line.strip() for line in lines]

def add_tuple(first, second):
    return tuple(a + b for a, b in zip(first, second))

part_1 = 0

for i in range(0,len(lines),4):
    print(i)
# for i in range(0,4,4):
    match_a = re.search(r'Button A: X\+(\d+), Y\+(\d+)', lines[i])
    a_x, a_y, a_cost = int(match_a.group(1)), int(match_a.group(2)), 3

    match_b = re.search(r'Button B: X\+(\d+), Y\+(\d+)', lines[i+1])
    b_x, b_y, b_cost = int(match_b.group(1)), int(match_b.group(2)), 1

    match_prize = re.search(r'Prize: X=(\d+), Y=(\d+)', lines[i+2])
    prize_x, prize_y = int(match_prize.group(1)) + 10000000000000, int(match_prize.group(2)) + 10000000000000

    A = np.array([[a_x, b_x], [a_y, b_y]])
    b = np.array([prize_x, prize_y])

    x1_bounds = range(0, 10**8)  # Bounds for x1 (0 to 10 inclusive)
    x2_bounds = (0, 10**8)
    # candidates = product(*[range(bound[0], bound[1] + 1) for bound in bounds])

    solutions = []
    for x1 in x1_bounds:
        # Solve for x2 using the first equation: A[0,0] * x1 + A[0,1] * x2 = b[0]
        remainder = b[0] - A[0, 0] * x1
        if remainder % A[0, 1] == 0:  # Check if x2 is an integer
            x2 = remainder // A[0, 1]
            
            # Check if x2 is within bounds
            if x2_bounds[0] <= x2 <= x2_bounds[1]:
                # Verify solution satisfies the second equation
                if A[1, 0] * x1 + A[1, 1] * x2 == b[1]:
                    solutions.append([x1, x2])

    if solutions:
        cost = float('inf')

        for sol in solutions:
            sol_cost = sol[0] * a_cost + sol[1] * b_cost
            if sol_cost < cost:
                cost = sol_cost
        
        part_1 += cost

    # combination = np.linalg.inv(left_side).dot(right_side)
    # combination = np.linalg.solve(left_side, right_side)
    # print(combination)
    # num_a, num_b = int(combination[0]), int(combination[1])

    # if a_x*num_a + b_x*num_b == prize_x and a_y*num_a + b_y*num_b == prize_y:
    #     part_1 += num_a * a_cost + num_b * b_cost

print('Part 1:', int(part_1))
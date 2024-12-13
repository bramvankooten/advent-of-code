import numpy as np
lines = open("data/9.out", "r").read()

full = [int(x) for x in list(lines)]
nums = full[::2]
gaps = full[1::2]

checksum = []
for i in range(len(nums)):
    checksum.extend([i] * nums[i])

checksum_rev = list(reversed(checksum))

index = 0
for i in range(len(nums)-1):
    index += nums[i]
    to_add = checksum_rev[:gaps[i]]
    checksum_rev = checksum_rev[gaps[i]:]
    checksum[index:index] = to_add
    index += gaps[i]

    if index >= sum(nums):
        break

checksum = checksum[:sum(nums)]

part_1 = 0
for i in range(len(checksum)):
    part_1 += i*checksum[i]

print('Part 1:', part_1)

checksum = []
for i in range(len(nums)-1):
    checksum.extend([i] * nums[i])
    checksum.extend(['.'] * gaps[i])

checksum.extend([i+1] * nums[-1])
checksum.extend(['.'])


nums_copy = nums.copy()

num = len(nums) - 1

for i in range(1,len(nums)):
    amount = nums[-i]
    for j in range(len(gaps)-(i-1)):
        if amount <= gaps[j]:
            gap_start = sum(gaps[:j]) + sum(nums_copy[:j+1])
            checksum[gap_start:gap_start+amount] = [num] * amount
            original_loc = -(sum(nums_copy[num:]) + sum(gaps[num:]) + 1)
            for a in range(amount):
                checksum[original_loc+a] = '.'
            gaps[j] -= amount
            nums_copy[j] += amount
            nums_copy[-i] -= amount
            gaps[-i] += amount
            
            break
    num -= 1

part_2 = 0

for i in range(len(checksum)-1):
    if not checksum[i] == '.':
        part_2 += i*checksum[i]

print('Part 2:', part_2)

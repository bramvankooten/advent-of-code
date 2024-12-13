import re

lines = open("data/7.out", "r").readlines()

lines = [line.strip() for line in lines]

processed = []
for line in lines:
    reg = re.search(r'^(\d+): (.+)', line)
    processed.append([int(reg.group(1)), list(map(int, reg.group(2).split()))])

part_1 = 0

def check_answer(answer, nums):
    options = [nums[0]]
    for i in range(1,len(nums)):
        new_options = []
        for o in options:
            mult = o * nums[i]
            add = o + nums[i]

            if mult <= answer:
                new_options.append(mult)
            if add <= answer:
                new_options.append(add)
        options = new_options
    if answer in options:
        return answer
    else:
        return 0

for p in processed:
    answer = p[0]
    nums = p[1]
    part_1 += check_answer(answer, nums)

print('Part 1:', part_1)

part_2 = 0

def check_answer_2(answer, nums):
    options = [nums[0]]
    for i in range(1,len(nums)):
        new_options = []
        for o in options:
            mult = o * nums[i]
            add = o + nums[i]
            concat = int(str(o) + str(nums[i]))

            if mult <= answer:
                new_options.append(mult)
            if add <= answer:
                new_options.append(add)
            if concat <= answer:
                new_options.append(concat)
        options = new_options
    if answer in options:
        return answer
    else:
        return 0

for p in processed:
    answer = p[0]
    nums = p[1]
    part_2 += check_answer_2(answer, nums)

print('Part 2:', part_2)
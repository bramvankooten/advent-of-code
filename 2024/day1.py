lines = open("data/1.out", "r").readlines()

first = []
second = []

for line in lines:
    nums = line.strip().split('   ')
    first.append(int(nums[0]))
    second.append(int(nums[1]))

first.sort()
second.sort()

dif_1 = 0

for i in range(len(first)):
    dif_1 += abs(first[i] - second[i])

print('Part 1:', dif_1)


similarity = 0

for num in first:
    similarity += second.count(num) * num

print('Part 2:', similarity)
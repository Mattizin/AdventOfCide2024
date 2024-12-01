print("Day 01 Part 01:")
# file = "1_test"
file = "1_puzzle"
with open(f'aoc2024/day01/data/{file}.txt') as f:
    lines = f.readlines()

list1 = []
list2 = []
for line in lines:
    line = line.rstrip()
    
    if(line == ""):
        continue

    nums = list(filter(lambda s: s != "", line.split(" ")))
    list1.append(int(nums[0]))
    list2.append(int(nums[1]))

list1.sort()
list2.sort()

distances = []
for idx, x in enumerate(list1):
    distances.append(abs(x-list2[idx]))

print(sum(distances))
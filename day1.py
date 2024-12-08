leftList = []
rightList = []
lines = []

with open("day1.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    split = line.strip().split("   ")
    leftList.append(int(split[0]))
    rightList.append(int(split[1]))

leftList.sort()
rightList.sort()
sum = 0
for i in range(len(leftList)):
    sum = sum + abs(leftList[i] - rightList[i])
print(sum)


# Part 2
sum2 = 0
for i in range(len(leftList)):
    sum2 = sum2 + (leftList[i] * rightList.count(leftList[i]))

print(sum2)
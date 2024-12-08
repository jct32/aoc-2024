import re

lines = []

with open("day3.txt", "r") as f:
    lines = f.readlines()

sum = 0

for line in lines:
    x = re.findall("mul\(\d*,\d*\)", line)
    for match in x:
        match = match[4:-1].split(',')
        sum += (int(match[0]) * int(match[1]))
print(sum)

sum = 0

multiplyAllowed = True
for line in lines:
    x = re.findall("mul\(\d*,\d*\)|don't|do", line)
    for match in x:
        if match == "don't":
            multiplyAllowed = False
        elif match == "do":
            multiplyAllowed = True
        else:
            if multiplyAllowed:
                match = match[4:-1].split(',')
                sum += (int(match[0]) * int(match[1]))
print(sum)
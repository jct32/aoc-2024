from utils import getLines
from functools import cmp_to_key

lines = getLines("day5.txt")

rules = []
pages = []

def is_valid_order(set, rules):
    for i in range(len(set) - 1):
        if(set[i+1], set[i]) in rules:
            return False
    return True

for line in lines:
    if '|' in line:
        x,y = line.split('|')
        rules.append((int(x),int(y)))
    elif ',' in line:
        values = line.split(',')
        values = [int(x) for x in values]
        pages.append(values)

sum = 0

for set in pages:
    correctOrder = True
    for rule in rules:
        if rule[0] in set and rule[1] in set:
            firstIndex = set.index(rule[0])
            secondIndex = set.index(rule[1])
            if firstIndex > secondIndex:
                correctOrder = False
    if correctOrder:
        sum += set[len(set)//2]

print(sum)

sum = 0

from functools import cmp_to_key
key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))

for set in pages:
    if set != (new_row := sorted(set, key=key)):
        sum += new_row[len(new_row)//2]

print(sum)
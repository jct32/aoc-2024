from utils import getLines
from itertools import combinations

def check_bounds(coordinates, bounds):
    for i in range(0, len(coordinates)):
        if coordinates[i] < 0 or coordinates[i] > (bounds[i] - 1):
            return False
    return True

lines = getLines("day8.txt")

width = len(lines[0])
height = len(lines)
antenna_type_installed = set()
for line in lines:
    for char in line:
        if char != '.':
            antenna_type_installed.add(char)

anti_node_locations = set()

for antenna in antenna_type_installed:
    locations = []
    combos = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == antenna:
                locations.append((i,j))
    for combo in combinations(locations, 2):
        combos += 1
        diff = (combo[0][0] - combo[1][0], combo[0][1] - combo[1][1])
        anti_nodes = []
        anti_nodes.append((combo[0][0] + diff[0], combo[0][1] + diff[1]))
        anti_nodes.append((combo[1][0] - diff[0], combo[1][1] - diff[1]))
        #out left or right
        for anti_node in anti_nodes:
            if check_bounds(anti_node, (height, width)):
                anti_node_locations.add(anti_node)
print(len(anti_node_locations))

anti_node_locations = set()

for antenna in antenna_type_installed:
    locations = []
    combos = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] == antenna:
                locations.append((i,j))
    for combo in combinations(locations, 2):
        anti_node_locations.add((combo[0][0], combo[0][1]))
        anti_node_locations.add((combo[1][0], combo[1][1]))
        diff = (combo[0][0] - combo[1][0], combo[0][1] - combo[1][1])
        # addition loop
        answer = (combo[0][0] + diff[0], combo[0][1] + diff[1])
        while check_bounds(answer, (height, width)):
            anti_node_locations.add(answer)
            answer = (answer[0] + diff[0], answer[1] + diff[1])
        answer = (combo[1][0] - diff[0], combo[1][1] - diff[1])
        # subtraction loop
        while check_bounds(answer, (height, width)):
            anti_node_locations.add(answer)
            answer = (answer[0] - diff[0], answer[1] - diff[1])

print(len(anti_node_locations))

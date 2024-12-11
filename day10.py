from utils import getLines

lines = getLines("day10.txt")

start_positions = []

def find_summit(position, map, part2):
    # Directions
    # 0 start
    # 1 left
    # 2 right
    # 3 up
    # 4 down
    currentValue = map[position[0]][position[1]]
    if currentValue == '9':
        if part2:
            summits.append((position[0], position[1]))
        else:
            summits.add((position[0], position[1]))
    direction = position[2]
    height = len(map)
    width = len(map[position[0]])
    potential_nodes = []
    # check left
    if position[1] > 0:
        potential_nodes.append((position[0], position[1] - 1, 1))
    # check right
    if position[1] < width - 1:
        potential_nodes.append((position[0], position[1] + 1, 2))
    # check up
    if position[0] > 0:
        potential_nodes.append((position[0] - 1, position[1], 3))
    # check down
    if position[0] < height - 1:
        potential_nodes.append((position[0] + 1, position[1], 4))

    for node in potential_nodes:
        y, x = node[0], node[1]
        if int(map[y][x]) == (int(currentValue) + 1):
            find_summit(node, map, part2)

for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == "0":
            start_positions.append((i, j, 0))

sum = 0
for start in start_positions:
    summits = set()
    find_summit(start, lines, False)
    sum += len(summits)
print(sum)

sum = 0
for start in start_positions:
    summits = []
    find_summit(start, lines, True)
    sum += len(summits)
print(sum)
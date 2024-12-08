from utils import getLines

def inside_bound(position):
    if position[0] < 0 or position[0] >= len(lines):
        return False
    elif position[1] < 0 or position[1] >= len(lines[position[0]]):
        return False
    else:
        return True
    
def inside_bound_part2(position, visits):
    global part2sum
    if len(visits) >= 8:
        for i in range(4, len(visits)//2 + 1):
            if visits[-i:] == visits[-i*2:-i]:
                part2sum += 1
                return False  
        return inside_bound(position)
    else:
        return inside_bound(position)
    
def move(current_position, direction):
    if direction == "up":
        if current_position[0] - 1 < 0:
            current_position = (current_position[0] - 1, current_position[1])
        elif lines[current_position[0] - 1][current_position[1]] == "#":
            direction = "right"
            if part2:
                visited_positions.append(current_position)
        else:
            current_position = (current_position[0] - 1, current_position[1])
    elif direction == "right":
        if current_position[1] + 1 >= len(lines[current_position[0]]):
            current_position = (current_position[0], current_position[1] + 1)
        elif lines[current_position[0]][current_position[1] + 1] == "#":
            direction = "down"
            if part2:
                visited_positions.append(current_position)
        else:
            current_position = (current_position[0], current_position[1] + 1)
    elif direction == "down":
        if current_position[0] + 1 >= len(lines):
            current_position = (current_position[0] + 1, current_position[1])
        elif lines[current_position[0] + 1][current_position[1]] == "#":
            direction = "left"
            if part2:
                visited_positions.append(current_position)
        else:
            current_position = (current_position[0] + 1, current_position[1])
    elif direction == "left":
        if current_position[1] - 1 < 0:
            current_position = (current_position[0], current_position[1] - 1)
        elif lines[current_position[0]][current_position[1] - 1] == "#":
            direction = "up"
            if part2:
                visited_positions.append(current_position)
        else:
            current_position = (current_position[0], current_position[1] - 1)
    if not part2:
        visited_positions.add(current_position)
    return current_position, direction


lines = getLines("day6.txt")

starting_position = None
visited_positions = None
start_found = False
direction = "up"

part2 = False
for i in range(0, len(lines)):
    if start_found:
        break
    for j in range (0, len(lines[i])):
        if lines[i][j] == '^':
            starting_position = (i, j)
            visited_positions = set([(i,j)])
            start_found = True
            break
# Now we go on the map until we are done
current_position = starting_position
while(inside_bound(current_position)):
    current_position, direction = move(current_position, direction)

print(len(visited_positions) - 1)

visited_positions = []
part2sum = 0
part2 = True
import time
start_time = time.time()
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        visited_positions.clear()
        if (i, j) == starting_position:
            continue
        else:
            current_position = starting_position
            direction = "up"
            if lines[i][j] == ".":
                lines[i] = lines[i][:j] + "#" + lines[i][j+1:]
                while(inside_bound_part2(current_position, visited_positions)):
                    current_position, direction = move(current_position, direction)
                lines[i] = lines[i][:j] + "." + lines[i][j+1:]
            
end_time = time.time()
print(end_time-start_time)
print(part2sum)

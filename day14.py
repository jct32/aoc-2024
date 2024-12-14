from utils import getLines

class Robot:
    def __init__(self, position, velocity):
        self.x = int(position[0])
        self.y = int(position[1])
        self.vel_x = int(velocity[0])
        self.vel_y = int(velocity[1])

    def increment(self):
        self.x += self.vel_x
        self.y += self.vel_y
        
        #check left wrap
        if self.x < 0:
            self.x += width
        #check right wrap
        if self.x > width - 1:
            self.x -= width
        #check down wrap
        if self.y > height - 1:
            self.y -= height
        #check up wrap
        if self.y < 0:
            self.y += height

    def print_location(self):
        print(f"x: {self.x}, y:{self.y}")

    def get_quardrant(self):
        x_divide = width // 2
        y_divide = height // 2
        if self.x == x_divide or self.y == y_divide:
            return 0
        if self.x < x_divide and self.y < y_divide:
            return 1
        elif self.x > x_divide and self.y < y_divide:
            return 2
        elif self.x < x_divide and self.y > y_divide:
            return 3
        elif self.x > x_divide and self.y > y_divide:
            return 4
        else:
            print("We made a boo-boo")

    def get_position(self):
        return self.x, self.y

def create_grid():
    grid = []
    for i in range(0, height):
        line = ''
        for j in range(0, width):
            line += '.'
        line += '\n'
        grid.append(line)
    return grid

lines = getLines("day14.txt")

width = 101
height = 103

robot_list = []

for line in lines:
    data = line.split(" ")
    position = data[0].split("=")[1].split(',')
    velocity = data[1].split("=")[1].split(',')
    robot = Robot(position, velocity)
    robot_list.append(robot)

minimum = 99999999999999999999999
minumum_time = -1
for i in range(0, 10000):
    grid = create_grid()
    quadrants = [0, 0, 0, 0]
    for robot in robot_list:
        robot.increment()
        x, y = robot.get_position()
        grid[y] = grid[y][:x] + "#" + grid[y][x+1:]
        quadrant = robot.get_quardrant()
        if quadrant != 0:
            quadrants[quadrant-1] += 1

    with open("trees.txt", "a") as f:
        f.write(f"i: {i+1}\n")
        f.writelines(grid)
        f.write("\n\n")
    
    sum = 1
    for quadrant in quadrants:
        sum *= quadrant
    if sum < minimum:
        minimum = sum
        minumum_time = i+1
    
    if i == 99:
        print(sum)

print(minumum_time)
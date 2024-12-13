from utils import getLines

lines = getLines("day13.txt")

def get_GCD(a,b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = get_GCD(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def find_cost(a, b, prize):
    a_cost = 3
    b_cost = 1
    minimum_cost = 1000
    actual_cost = 0
    for i in range(0, 101):
        for j in range(0, 101):
            x_total = (i*a[0] + j*b[0])
            y_total = (i*a[1] + j*b[1])
            if x_total == prize[0] and y_total == prize[1]:
                cost = i*a_cost + j*b_cost
                if cost < minimum_cost:
                    actual_cost = cost
                    minimum_cost = cost
    return actual_cost

def find_cost2(a, b, prize):
    prize = (prize[0]+10000000000000, prize[1]+10000000000000)
    determinate = a[0] * b[1] - b[0] * a[1]
    a_num = prize[0] * b[1] - prize[1] * b[0]
    b_num = prize[0] * a[1] - prize[1] * a[0]
    if any([determinate == 0, a_num % determinate != 0,
            b_num % determinate !=0]):
        return 0
    a, b = a_num // determinate, -b_num // determinate
    return 3 * a + b

sum = 0
sum2 = 0
for i in range(0, len(lines) -2, 4):
    button_a = lines[i]
    button_b = lines[i+1]
    prize = lines[i+2]
    button_a = button_a.split(": ")[1].split(", ")
    button_a = (int(button_a[0].split('X+')[1]), int(button_a[1].split("Y+")[1]))
    button_b = button_b.split(": ")[1].split(", ")
    button_b = (int(button_b[0].split('X+')[1]), int(button_b[1].split("Y+")[1]))
    prize = prize.split(": ")[1].split(", ")
    prize = (int(prize[0].split('X=')[1]), int(prize[1].split("Y=")[1]))
    sum += find_cost(button_a, button_b, prize)
    sum2+= find_cost2(button_a,button_b, prize)

print(sum)
print(sum2)
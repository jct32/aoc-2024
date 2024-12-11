from utils import getLines

stones_dict = {}

def stone_simulation(stones):
    new_dict = {}
    for stone in stones:
        if stone == '0':
            if '1' in new_dict:
                new_dict['1'] += stones[stone]
            else:
                new_dict['1'] = stones[stone]
        elif len(stone) % 2 == 0:
            first_half = stone[:len(stone)//2].lstrip('0')
            second_half = stone[len(stone)//2:].lstrip('0')
            if first_half == '':
                first_half = '0'
            if second_half == '':
                second_half = '0'
            if first_half in new_dict:
                new_dict[first_half] += stones[stone]
            else:
                new_dict[first_half] = stones[stone]
            if second_half in new_dict:
                new_dict[second_half] += stones[stone]
            else:
                new_dict[second_half] = stones[stone]
        else:
            new_stone = str(int(stone) * 2024)
            if new_stone in new_dict:
                new_dict[new_stone] += stones[stone]
            else:
                new_dict[new_stone] = stones[stone]
    return new_dict

lines = getLines("day11.txt")

stones = lines[0].split(" ")
for stone in stones:
    if stone in stones_dict:
        stones_dict[stone] += 1
    else:
        stones_dict[stone] = 1

for i in range(0, 25):
    stones_dict = stone_simulation(stones_dict)
sum = 0
for stone in stones_dict:
    sum += stones_dict[stone]
print(sum)

for i in range(0, 75):
    stones_dict = stone_simulation(stones_dict)
sum = 0
for stone in stones_dict:
    sum += stones_dict[stone]
print(sum)
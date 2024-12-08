from utils import getLines

lines = getLines("day4.txt")

SPECIAL_WORD = "XMAS"

def check_word(str):
    if str == SPECIAL_WORD or str == SPECIAL_WORD[::-1]:
        return 1
    else:
        return 0

def check_left(i, j):
    if j < 3:
        return 0
    else:
        str = ''
        for k in range(0, 4):
            str += lines[i][j-k]
        return check_word(str)
        
def check_up(i,j):
    if i < 3:
        return 0
    else:
        str = ''
        for k in range(0, 4):
            str += lines[i-k][j]
        return check_word(str)

def check_up_left(i,j):
    if i < 3 or j < 3:
        return 0
    else:
        str = ''
        for k in range(0, 4):
            str += lines[i-k][j-k]
        return check_word(str)

def check_down_left(i,j):
    if i > len(lines) - 4 or j < 3:
        return 0
    else:
        str = ''
        for k in range(0, 4):
            str += lines[i+k][j-k]
        return check_word(str)

def check_x_mas(i,j):
    if i < 1 or i > len(lines) - 2 or j < 1 or j > len(lines[i]) - 2:
        return 0
    else:
        str1 = lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1]
        str2 = lines[i+1][j-1] + lines[i][j] + lines[i-1][j+1]
        if check_word(str1) == 1 and check_word(str2) == 1:
            return 1
        else:
            return 0


#part 1
sum = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        sum += check_left(i,j)
        sum += check_up(i,j)
        sum += check_up_left(i,j)
        sum += check_down_left(i,j)
print(sum)

#part 2
SPECIAL_WORD = "MAS"
sum = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        sum += check_x_mas(i,j)
print(sum)
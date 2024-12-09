from utils import getLines

lines = getLines("day9.txt")

file_array = []

def sum_file(expanded_file):
    sum = 0
    for i in range(0, len(expanded_file)):
        if expanded_file[i] == '.':
            break
        else:
            sum += i * int(expanded_file[i])
    return sum

def part_1(file_array):
    expanded_file = file_array.copy()
    last_replaceIndex = len(expanded_file) - 1
    for i in range(0, len(expanded_file)):
        if expanded_file[i] == '.' and i < last_replaceIndex:
            while expanded_file[last_replaceIndex] == '.':
                last_replaceIndex -= 1
            expanded_file[i], expanded_file[last_replaceIndex] = expanded_file[last_replaceIndex], expanded_file[i]

    print(sum_file(expanded_file))

def part_2(file_array):
    expanded_file = file_array.copy()
    indexDisk = []
    last_file_type = expanded_file[0]
    size = 1
    for i in range(1, len(expanded_file)):
        if i == len(expanded_file) - 1:
            if expanded_file[i] == last_file_type:
                indexDisk.append((last_file_type, size + 1))
            else:
                indexDisk.append((expanded_file[i], 1))
        if expanded_file[i] != last_file_type:
            indexDisk.append((last_file_type, size))
            size = 1
        else:
            size += 1
        last_file_type = expanded_file[i]
    
    i = 0
    while i < len(indexDisk):
        if indexDisk[i][0] == '.':
            j = len(indexDisk) - 1
            while j >= 0 and j > i:
                if indexDisk[j][0] == '.':
                    j -= 1
                    continue
                if indexDisk[j][1] == indexDisk[i][1]:
                    indexDisk[i], indexDisk[j] = indexDisk[j], indexDisk[i]
                    break
                elif indexDisk[j][1] < indexDisk[i][1]:
                    file_size = indexDisk[j][1]
                    file_type = indexDisk[j][0]
                    remainder = indexDisk[i][1] - indexDisk[j][1]
                    indexDisk[j] = ('.', file_size)
                    indexDisk[i] = (file_type, file_size)
                    indexDisk.insert(i+1, ('.', remainder))
                    break
                j -= 1
        i += 1
    
    sum = 0
    first_index = 0
    for i in range(0, len(indexDisk)):
        if indexDisk[i][0] != '.':
            for j in range(0, indexDisk[i][1]):
                sum += indexDisk[i][0] * (first_index + j)
        first_index += indexDisk[i][1]
    print(sum)

file_id = 0

for i in range(0, len(lines[0])):
    num_blocks = int(lines[0][i])
    for j in range(0, num_blocks):
        if i % 2 == 0:
            file_array.append(file_id)
        else:
            file_array += '.'
    if i % 2 == 0:
        file_id += 1
part_1(file_array)
part_2(file_array)
from utils import getLines
from itertools import combinations

lines = getLines("day7.txt")

def operate(nums, part2=True):
    if len(nums) == 1:
        yield nums[0]
        return
    for result in operate(nums[:-1]):
        yield result + nums[-1]
        yield result * nums[-1]
        if part2:
            yield int(str(result)+str(nums[-1]))




answer = 0
for line in lines:
    expected_answer = int(line.split(":")[0])
    operands = [int(value) for value in line.split(":")[1].strip().split(" ")]
    for result in operate(operands):
        if expected_answer == result:
            answer += expected_answer
            break

print(answer)
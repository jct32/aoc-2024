def getDirection(num1, num2):
    if num1 > num2:
        return -1
    elif num1 < num2:
        return 1
    else:
        return 0
    
from datetime import datetime
startTime = datetime.now()
lines = []
safeSum = 0

with open("day2.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    numbers = line.split(' ')
    numbers = [int(number) for number in numbers]
    numberGood = True
    direction = getDirection(numbers[0], numbers[1])
    if direction == 0:
        continue
    for i in range(1, len(numbers)):
        numberGood = False
        newDirection = getDirection(numbers[i-1], numbers[i])
        difference = abs(numbers[i-1] - numbers[i])
        if (newDirection != direction) or difference > 3:
            break
        numberGood = True
    if numberGood == True:
        safeSum += 1
print(safeSum)

dampenedSafe = 0

for line in lines:
    numbers = line.split(' ')
    numbers = [int(number) for number in numbers]
    corepos = set([1,2,3])
    coreneg = set([-1,-2,-3])
    safepos = set([1,2,3])
    safeneg = set([-1,-2,-3])
    goodRemoved = False
    for i in range(1, len(numbers)):
        safepos.add(numbers[i] - numbers[i-1])
        safeneg.add(numbers[i] - numbers[i-1])
    if len(safepos) == 3 or len(safeneg) == 3:
        dampenedSafe += 1

    if len(safepos) > 3:
        i = 0
        bootedOne = False
        newpos = corepos.copy()
        newNumbers = numbers.copy()
        while i < len(newNumbers) - 1:
            if newNumbers[i+1] - newNumbers[i] not in corepos:
                if bootedOne == False:
                    del newNumbers[i]
                    bootedOne = True
                    if i != 0:
                        i -= 1
                    continue
            newpos.add(newNumbers[i+1] - newNumbers[i])
            i += 1
        if len(newpos) == 3:
            dampenedSafe += 1
            goodRemoved = True
        else:
            bootedOne = False
            i = 0
            newpos = corepos.copy()
            newNumbers = numbers.copy()
            while i < len(newNumbers) - 1:
                if newNumbers[i+1] - newNumbers[i] not in corepos:
                    if bootedOne == False:
                        del newNumbers[i+1]
                        bootedOne = True
                        if i != 0:
                            i -= 1
                        continue
                newpos.add(newNumbers[i+1] - newNumbers[i])
                i += 1
            if len(newpos) == 3:
                dampenedSafe += 1
                goodRemoved = True

    if len(safeneg) > 3 and not goodRemoved:
        i = 0
        bootedOne = False
        newneg = coreneg.copy()
        newNumbers = numbers.copy()
        while i < len(newNumbers) - 1:
            if newNumbers[i+1] - newNumbers[i] not in coreneg:
                if bootedOne == False:
                    del newNumbers[i]
                    bootedOne = True
                    if i != 0:
                        i -= 1
                    continue
            newneg.add(newNumbers[i+1] - newNumbers[i])
            i += 1
        if len(newneg) == 3:
            dampenedSafe += 1
        else:
            bootedOne = False
            i = 0
            newneg = coreneg.copy()
            newNumbers = numbers.copy()
            while i < len(newNumbers) - 1:
                if newNumbers[i+1] - newNumbers[i] not in coreneg:
                    if bootedOne == False:
                        del newNumbers[i+1]
                        bootedOne = True
                        if i != 0:
                            i -= 1
                        continue
                newneg.add(newNumbers[i+1] - newNumbers[i])
                i += 1
            if len(newneg) == 3:
                dampenedSafe += 1
    

print(dampenedSafe)
print(datetime.now() - startTime)
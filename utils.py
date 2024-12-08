def getLines(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    return lines
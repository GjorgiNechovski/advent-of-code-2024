file = '1.txt'

data = open(file).read().strip()
grid = data.split('\n')
numRows = len(grid)
numCols = len(grid[0])
frequencies = {}

for row in range(numRows):
    for column in range(numCols):
        if grid[row][column] != '.':
            if grid[row][column] not in frequencies:
                frequencies[grid[row][column]] = []

            frequencies[grid[row][column]].append((row, column))

partOneSet = set()
partTwoSet = set()

for row in range(numRows):
    for column in range(numCols):
        for frequency, frequenciesList in frequencies.items():
            for (row1, col1) in frequenciesList:
                for (row2, col2) in frequenciesList:
                    if (row1, col1) != (row2, col2):
                        distance1 = abs(row - row1) + abs(column - col1)
                        distance2 = abs(row - row2) + abs(column - col2)
                        verticalDistance1 = row - row1
                        verticalDistance2 = row - row2
                        horizontalDistance1 = column - col1
                        horizontalDistance2 = column - col2

                        if (distance1 == 2 * distance2 or distance1 * 2 == distance2) and 0 <= row < numRows and 0 <= column < numCols and (verticalDistance1 * horizontalDistance2 == horizontalDistance1 * verticalDistance2):
                            partOneSet.add((row, column))
                        if 0 <= row < numRows and 0 <= column < numCols and (verticalDistance1 * horizontalDistance2 == horizontalDistance1 * verticalDistance2):
                            partTwoSet.add((row, column))

p1 = len(partOneSet)
p2 = len(partTwoSet)

print(p1)
print(p2)

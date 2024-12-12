from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

infile = '2.txt'
p1 = 0
p2 = 0
fileData = open(infile).read().strip()

data = fileData.split('\n')
boundX = len(data)
boundY = len(data[0])

visited = set()

def dfs(row, col, visited, grid, directionInfo):
    stack = [(row, col)]
    area = 0
    perimeter = 0
    while stack:
        currRow, currCol = stack.pop()
        if (currRow, currCol) in visited:
            continue
        visited.add((currRow, currCol))
        area += 1

        for dirX, dirY in DIRECTIONS:
            newRow = currRow + dirX
            newCol = currCol + dirY

            if 0 <= newRow < boundX and 0 <= newCol < boundY and grid[newRow][newCol] == grid[currRow][currCol]:
                stack.append((newRow, newCol))
            else:
                perimeter += 1
                if (dirX, dirY) not in directionInfo:
                    directionInfo[(dirX, dirY)] = set()
                directionInfo[(dirX, dirY)].add((currRow, currCol))

    return area, perimeter

def calculateSides(directionInfo):
    sides = 0
    for direction, positions in directionInfo.items():
        visitedPerimeter = set()
        for (currRow, currCol) in positions:
            if (currRow, currCol) not in visitedPerimeter:
                sides += 1
                queue = deque([(currRow, currCol)])
                while queue:
                    row2, col2 = queue.popleft()
                    if (row2, col2) in visitedPerimeter:
                        continue
                    visitedPerimeter.add((row2, col2))
                    for dirX, dirY in DIRECTIONS:
                        newRow, newCol = row2 + dirX, col2 + dirY
                        if (newRow, newCol) in positions:
                            queue.append((newRow, newCol))
    return sides

for row in range(boundX):
    for col in range(boundY):
        if (row, col) in visited:
            continue

        directionInfo = dict()
        area, perimeter = dfs(row, col, visited, data, directionInfo)
        sides = calculateSides(directionInfo)

        p1 += area * perimeter
        p2 += area * sides

print(p1)
print(p2)

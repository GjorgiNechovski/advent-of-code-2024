from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

infile = '1.txt'
data = open(infile).read().strip()

grid = data.split('\n')
rowLenght = len(grid)
colLenght = len(grid[0])
grid = [[grid[r][c] for c in range(colLenght)] for r in range(rowLenght)]

for r in range(rowLenght):
    for c in range(colLenght):
        if grid[r][c] == 'S':
            startRow,startCol = r,c
        if grid[r][c] == 'E':
            endRow,endCol = r,c

distances = {}
queue = deque([(0, endRow, endCol)])

while queue:
    d,r,c = queue.popleft()
    if (r,c) in distances:
        continue

    distances[(r, c)] = d

    for dr,dc in directions:
        nextRow,nextCol = r + dr, c + dc
        if 0<=nextRow<rowLenght and 0<=nextCol<colLenght and grid[nextRow][nextCol]!= '#':
            queue.append((d + 1, nextRow, nextCol))

def exec(initialDistance, cheatTime):
    result = set()
    queue = deque([(0, None, None, None, startRow, startCol)])

    visited = set()
    margin = 100

    while queue:
        distance,timeStart,timeEnd,time,row,col = queue.popleft()
        if distance>=initialDistance-margin:
            continue
        if grid[row][col] == 'E':
            if timeEnd is None:
                timeEnd = (row,col)
            if distance<=initialDistance-margin and (timeStart, timeEnd) not in result:
                result.add((timeStart, timeEnd))

        if (row,col,timeStart,timeEnd,time) in visited:
            continue
        visited.add((row,col,timeStart,timeEnd,time))


        if timeStart is None:
            queue.append((distance, (row,col), None, cheatTime, row, col))
        if time is not None and grid[row][col]!= '#':
            if distances[(row, col)] <= initialDistance-100-distance:
                result.add((timeStart, (row,col)))
        if time == 0:
            continue
        else:
            for dirRow,dirCol in directions:
                nextRow,nextCol = row+dirRow, col+dirCol
                if time is not None:
                    if 0<=nextRow<rowLenght and 0<=nextCol<colLenght:
                        queue.append((distance+1,timeStart,None,time-1,nextRow,nextCol))
                else:
                    if 0<=nextRow<rowLenght and 0<=nextCol<colLenght and grid[nextRow][nextCol]!= '#':
                        queue.append((distance+1,timeStart,timeEnd,time,nextRow,nextCol))
    return len(result)

distance = distances[(startRow, startCol)]

print(exec(distance, 2))
print(exec(distance, 20))
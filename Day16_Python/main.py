import heapq

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

infile ='1.txt'
fileData = open(infile).read().strip()

grid = fileData.split('\n')
rowNum = len(grid)
colNum = len(grid[0])
grid = [[grid[r][c] for c in range(colNum)] for r in range(rowNum)]

for r in range(rowNum):
    for c in range(colNum):
        if grid[r][c] == 'S':
            sr,sc = r,c
        if grid[r][c] == 'E':
            er,ec = r,c

queue = []
visited = set()
heapq.heappush(queue, (0, sr, sc, 1))
distance = {}
bestPath = None

while queue:
    currentDistance,r,c,dir = heapq.heappop(queue)
    if (r,c,dir) not in distance:
        distance[(r, c, dir)] = currentDistance

    if r==er and c==ec and bestPath is None:
        bestPath = currentDistance

    if (r,c,dir) in visited:
        continue

    visited.add((r, c, dir))
    nextDirRow,newxtDirCol = directions[dir]
    nextRow,nextCol = r + nextDirRow, c + newxtDirCol
    if 0<=nextCol<colNum and 0<=nextRow<rowNum and grid[nextRow][nextCol] != '#':
        heapq.heappush(queue, (currentDistance + 1, nextRow, nextCol, dir))

    heapq.heappush(queue, (currentDistance + 1000, r, c, (dir + 1) % 4))
    heapq.heappush(queue, (currentDistance + 1000, r, c, (dir + 3) % 4))

print(bestPath)

queue = []
visited = set()
for dir in range(4):
    heapq.heappush(queue, (0, er, ec, dir))

distance2 = {}

while queue:
    currentDistance,r,c,dir = heapq.heappop(queue)
    if (r,c,dir) not in distance2:
        distance2[(r, c, dir)] = currentDistance

    if (r,c,dir) in visited:
        continue

    visited.add((r, c, dir))
    nextDirRow,newxtDirCol = directions[(dir + 2) % 4]
    nextRow,nextCol = r + nextDirRow, c + newxtDirCol

    if 0<=nextCol<colNum and 0<=nextRow<rowNum and grid[nextRow][nextCol] != '#':
        heapq.heappush(queue, (currentDistance + 1, nextRow, nextCol, dir))

    heapq.heappush(queue, (currentDistance + 1000, r, c, (dir + 1) % 4))
    heapq.heappush(queue, (currentDistance + 1000, r, c, (dir + 3) % 4))

optimalPath = set()
for r in range(rowNum):
    for c in range(colNum):
        for dir in range(4):
            if (r,c,dir) in distance and (r, c, dir) in distance2 and distance[(r, c, dir)] + distance2[(r, c, dir)] == bestPath:
                optimalPath.add((r, c))

print(len(optimalPath))
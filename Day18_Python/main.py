from collections import deque

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

file = '1.txt'
data = open(file).read().strip()

gridSize = 71
grid = [['.' for c in range(gridSize)] for r in range(gridSize)]

for i,line in enumerate(data.split('\n')):
    x,y = [int(x) for x in line.split(',')]
    if 0<=y<gridSize and 0<=x<gridSize:
        grid[y][x] = '#'

    queue = deque([(0, 0, 0)])
    visited = set()
    hasPath = False

    while queue:
        distance,row,col = queue.popleft()
        if (row, col) == (gridSize - 1, gridSize - 1):
            if i==1023: # byte size
                print(distance)
            hasPath = True
            break

        if (row, col) in visited:
            continue

        visited.add((row, col))
        for dr,dc in directions:
            nextRow = row + dr
            nextCol = col + dc
            if 0<=nextRow<gridSize and 0<=nextCol<gridSize and grid[nextRow][nextCol] != '#':
                queue.append((distance + 1, nextRow, nextCol))

    if not hasPath:
        print(f'{x},{y}')
        break
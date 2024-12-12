from collections import deque


def bfs(grid, startX, startY):
    rows = len(grid)
    cols = len(grid[0])

    visited = []
    for i in range(rows):
        visited.append([False] * cols)

    queue = deque([(startX, startY)])
    visited[startX][startY] = True
    reachableEnds = 0

    while queue:
        x, y = queue.popleft()

        if grid[x][y] == 9:
            reachableEnds += 1

        for dirX, dirY in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newX, newY = x + dirX, y + dirY
            if 0 <= newX < rows and 0 <= newY < cols and not visited[newX][newY]:
                if grid[newX][newY] == grid[x][y] + 1:
                    visited[newX][newY] = True
                    queue.append((newX, newY))

    return reachableEnds


def Exec(grid):
    rows = len(grid)
    cols = len(grid[0])
    sum = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                score = bfs(grid, x, y)
                sum += score

    return sum


def read(filename):
    with open(filename, 'r') as f:
        grid = []
        for line in f:
            grid.append([int(char) for char in line.strip()])
    return grid


filename = '1.txt'
grid = read(filename)

sum = Exec(grid)
print(sum)

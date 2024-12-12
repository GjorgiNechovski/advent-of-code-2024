def dfs(grid, startX, startY, usedStartingLocations):
    if (startX, startY) in usedStartingLocations:
        return usedStartingLocations[(startX, startY)]

    if grid[startX][startY] == 9:
        return 1

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newX, newY = startX + dx, startY + dy
        if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == grid[startX][startY] + 1:
            count += dfs(grid, newX, newY, usedStartingLocations)

    usedStartingLocations[(startX, startY)] = count
    return count


def Exec(grid):
    rows = len(grid)
    cols = len(grid[0])
    sum = 0
    usedStartingLocations = {}

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                rating = dfs(grid, x, y, usedStartingLocations)
                sum += rating

    return sum


def read(filename):
    with open(filename, 'r') as f:
        grid = []
        for line in f:
            grid.append([int(char) for char in line.strip()])
    return grid


filename = '2.txt'
grid = read(filename)

sum = Exec(grid)
print(sum)

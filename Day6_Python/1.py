def step(location, d, blockedCeil=None):
    di, dj = d
    while True:
        currentPosition = (location[0] + di, location[1] + dj)

        if grid.get(currentPosition) == "#" or currentPosition == blockedCeil:
            di, dj = dj, -di
        else:
            return currentPosition, (di, dj)


def exec(extra=None):
    visitedPairs = set()
    visited = set()
    location = next(k for k, v in grid.items() if v == "^")
    direction = (-1, 0)

    while location in grid:
        if (location, direction) in visitedPairs:
            break

        visitedPairs.add((location, direction))
        visited.add(location)

        location, direction = step(location, direction, extra)
    else:
        return visited

    return True


file='2.txt'


with open(file) as file:
    lines = file.read().splitlines()

grid = {}
for i, line in enumerate(lines):
    for j, character in enumerate(line):
        grid[(i, j)] = character


partOnePath = exec()
p1 = len(partOnePath)
print(p1)

p2 = sum(exec(location) is True for location in partOnePath)
print(p2)

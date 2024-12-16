def read(fileName):
    robots = []
    with open(fileName, 'r') as f:
        for line in f:
            pStr, vStr = line.split(' v=')
            p = tuple(map(int, pStr[2:].split(',')))
            v = tuple(map(int, vStr.split(',')))
            robots.append((p, v))
    return robots


def moveRobots(robots, width, height):
    newPositions = []
    for (px, py), (velX, velY) in robots:
        newPx = (px + velX) % width
        newPy = (py + velY) % height
        newPositions.append(((newPx, newPy), (velX, velY)))
    return newPositions


def draw(positions, width, height):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for px, py in positions:
        grid[py][px] = '1'
    for row in grid:
        print(''.join(row))


def getPositions(robot, t, width, height):
    (px, py), (vx, vy) = robot
    return ((px + vx * t) % width, (py + vy * t) % height)


def findTree(robots, width, height, iterationsLimit=10000):
    for t in range(iterationsLimit):
        positions = [getPositions(robot, t, width, height) for robot in robots]
        draw(positions, width, height)

        adj = countConnections(positions, width, height)
        if adj > 200:
            return t

    return None


def countConnections(positions, width, height):
    connections = 0
    posSet = set(positions)
    for y in range(height):
        for x in range(width - 1):
            if (x, y) in posSet and (x + 1, y) in posSet:
                connections += 1
    return connections


def robotsPerQuadrant(robots, width, height):
    topLeft = 0
    topRight = 0
    bottomLeft = 0
    bottomRight = 0

    for (px, py), _ in robots:
        if px == width // 2 or py == height // 2:
            continue

        if px < width // 2 and py < height // 2:
            topLeft += 1
        elif px >= width // 2 and py < height // 2:
            topRight += 1
        elif px < width // 2 and py >= height // 2:
            bottomLeft += 1
        elif px >= width // 2 and py >= height // 2:
            bottomRight += 1

    return topLeft, topRight, bottomLeft, bottomRight


def safetyFactor(robots, width, height):
    topLeft, topRight, botLeft, botRight = robotsPerQuadrant(robots, width, height)
    return topLeft * topRight * botLeft * botRight


def main():
    width = 101
    height = 103

    robots = read('1.txt')

    time = findTree(robots, width, height)

    print(time)


if __name__ == "__main__":
    main()

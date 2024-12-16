def read(file_name):
    robots = []
    with open(file_name, 'r') as f:
        for line in f:
            p_str, v_str = line.split(' v=')
            p = tuple(map(int, p_str[2:].split(',')))
            v = tuple(map(int, v_str.split(',')))
            robots.append((p, v))
    return robots


def moveRobots(robots, width, height):
    new_positions = []
    for (px, py), (velX, velY) in robots:
        newPx = (px + velX) % width
        newPy = (py + velY) % height
        new_positions.append(((newPx, newPy), (velX, velY)))
    return new_positions


def robotsPerQuadrant(robots, width, height):
    top_left = 0
    top_right = 0
    bottom_left = 0
    bottom_right = 0

    for (px, py), _ in robots:
        if px == width // 2 or py == height // 2:
            continue

        if px < width // 2 and py < height // 2:
            top_left += 1
        elif px >= width // 2 and py < height // 2:
            top_right += 1
        elif px < width // 2 and py >= height // 2:
            bottom_left += 1
        elif px >= width // 2 and py >= height // 2:
            bottom_right += 1

    return top_left, top_right, bottom_left, bottom_right


def safetyFactor(robots, width, height):
    topLeft, topRight, botLeft, botRight = robotsPerQuadrant(robots, width, height)
    return topLeft * topRight * botLeft * botRight


def main():
    width = 101
    height = 103

    robots = read('1.txt')

    for _ in range(100):
        robots = moveRobots(robots, width, height)

    factor = safetyFactor(robots, width, height)
    print(f"Safety factor after 100 seconds: {factor}")


if __name__ == "__main__":
    main()

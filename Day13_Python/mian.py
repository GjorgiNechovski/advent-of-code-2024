with open('1.txt') as f:
    lines = [line.rstrip() for line in f]


def solve(part: int):
    cost = 0
    if part == 2:
        offset = 10000000000000
    else:
        offset = 0
    for line in lines:
        if line.startswith("Button"):
            lineDetails = line.split(" ")

            a = lineDetails[1].split(":")[0]
            if a == 'A':
                x1 = int(lineDetails[2][2:-1])
                y1 = int(lineDetails[3][2:])
            else:
                x2 = int(lineDetails[2][2:-1])
                y2 = int(lineDetails[3][2:])

        elif line.startswith("Prize"):
            lineDetails = line.split(" ")

            p1 = int(lineDetails[1][2:-1]) + offset
            p2 = int(lineDetails[2][2:]) + offset
            a = (p1 * y2 - p2 * x2) / (x1 * y2 - y1 * x2)
            b = (p2 * x1 - p1 * y1) / (x1 * y2 - y1 * x2)

            if a == int(a) and b == int(b):
                cost += int(3 * a + b)

    print(cost)


solve(1)
solve(2)
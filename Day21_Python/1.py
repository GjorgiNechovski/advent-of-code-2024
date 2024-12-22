
def bestPath(x, y, dx, dy, robots, invalid):
    ret = None
    graph = [(x, y, "")]

    while len(graph) > 0:
        x, y, path = graph.pop(0)

        if x == dx and y == dy:
            temp = bestRobot(path + "A", robots - 1)
            ret = temp if ret is None else min(ret, temp)
        elif (x, y) != invalid:
            if x < dx:
                graph.append((x + 1, y, path + ">"))
            elif x > dx:
                graph.append((x - 1, y, path + "<"))
            if y < dy:
                graph.append((x, y + 1, path + "v"))
            elif y > dy:
                graph.append((x, y - 1, path + "^"))

    return ret

def bestRobot(path, robots):
    if robots == 1:
        return len(path)

    ret = 0
    pad = decode("X^A<v>", 3)
    x, y = pad["A"]

    for val in path:
        currX, currY = pad[val]
        ret += bestPath(x, y, currX, currY, robots, pad["X"])
        x, y = currX, currY

    return ret

def cheapest(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]

    while len(todo) > 0:
        x, y, path = todo.pop(0)

        if x == dx and y == dy:
            temp = bestRobot(path + "A", robots)
            ret = temp if ret is None else min(ret, temp)
        elif (x, y) != invalid:
            if x < dx:
                todo.append((x + 1, y, path + ">"))
            elif x > dx:
                todo.append((x - 1, y, path + "<"))
            if y < dy:
                todo.append((x, y + 1, path + "v"))
            elif y > dy:
                todo.append((x, y - 1, path + "^"))
    return ret

def decode(val, width):
    returnMe = {}

    for x, val in enumerate(val):
        returnMe[val] = (x % width, x // width)

    return returnMe

def exec(values, mode):
    ret = 0
    pad = decode("789456123X0A", 3)

    for row in values:
        result = 0
        x, y = pad["A"]

        for val in row:
            dirX, dirY = pad[val]
            result += cheapest(x, y, dirX, dirY, 3 if mode == 1 else 26, pad["X"])
            x, y = dirX, dirY
        ret += result * int(row[:-1].lstrip("0"))

    return ret
def run(data):
    print(exec(data, 1))
    print(exec(data, 2))

if __name__ == "__main__":
    fn = '1.txt'
    with open(fn) as f: data = [x.strip("\r\n") for x in f.readlines()]
    run(data)
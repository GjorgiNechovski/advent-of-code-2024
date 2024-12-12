def calc(values):
    rules = []
    result = 0
    for row in values:
        if "|" in row:
            rules.append(list(map(int, row.split("|"))))
        elif "," in row:
            row = list(map(int, row.split(",")))
            first = True
            while True:
                problems = []
                for a, b in rules:
                    if len(set([a, b]) & set(row)) == 2:
                        if row.index(a) > row.index(b):
                            problems.append((row.index(a), row.index(b)))
                            break

                if first and len(problems) == 0:
                    break
                first = False
                if len(problems) == 0:
                    result += row[(len(row) - 1) // 2]
                    break
                a, b = problems[0]
                row[a], row[b] = row[b], row[a]

    print(result)

def run(values):
    calc(values)

if __name__ == "__main__":
    fn = '2.txt'
    if fn is not None:
        with open(fn) as f:
            values = [x.strip("\r\n") for x in f.readlines()]
        run(values)

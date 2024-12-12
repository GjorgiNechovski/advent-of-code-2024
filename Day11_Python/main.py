from tqdm import tqdm

processedData = {}

def solve(element, transformTimes):
    if (element, transformTimes) in processedData:
        return processedData[(element, transformTimes)]

    if transformTimes == 0:
        ret = 1
    elif element == 0:
        ret = solve(1, transformTimes - 1)
    elif len(str(element)) % 2 == 0:
        parsedNumber = str(element)
        middle = len(parsedNumber) // 2
        left = int(parsedNumber[:middle])
        right = int(parsedNumber[middle:])
        ret = solve(left, transformTimes - 1) + solve(right, transformTimes - 1)
    else:
        ret = solve(element * 2024, transformTimes - 1)

    processedData[(element, transformTimes)] = ret
    return ret

def read(filename):
    with open(filename, 'r') as f:
        data = f.read().strip().split()
    return [int(x) for x in data]

filename = '1.txt'
data = read(filename)

def execAmountOfTimes(times):
    return sum(solve(element, times) for element in tqdm(data))

print(execAmountOfTimes(25))
print(execAmountOfTimes(75))

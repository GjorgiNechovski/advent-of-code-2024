with open('1.txt', 'r') as file:
    data = file.read().strip().split('\n\n')

availablePatterns = data[0].split(', ')
requiredPatterns = data[1].split('\n')

def calc(design, patterns):
    possibleWays = [0] * (len(design) + 1)
    possibleWays[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i-len(pattern):i] == pattern:
                possibleWays[i] += possibleWays[i-len(pattern)]

    return possibleWays[len(design)]

result = sum(calc(design, availablePatterns) for design in requiredPatterns)

print(result)

file = '1.txt'

part1 = 0
part2 = 0
data = open(file).read()

def isValid(targetNumber, numbers, isPart2):
    if len(numbers) == 1:
        return numbers[0]==targetNumber
    if isValid(targetNumber, [numbers[0] + numbers[1]] + numbers[2:], isPart2):
        return True
    if isValid(targetNumber, [numbers[0] * numbers[1]] + numbers[2:], isPart2):
        return True
    if isPart2 and isValid(targetNumber, [int(str(numbers[0]) + str(numbers[1]))] + numbers[2:], isPart2):
        return True
    return False

for line in data.strip().split('\n'):
    targetNumber, numbers = line.strip().split(':')
    targetNumber = int(targetNumber)
    numbers = [int(x) for x in numbers.strip().split()]

    if isValid(targetNumber, numbers, isPart2=False):
        part1 += targetNumber
    if isValid(targetNumber, numbers, isPart2=True):
        part2 += targetNumber

print(part1)
print(part2)
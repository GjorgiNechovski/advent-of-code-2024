from collections import deque

infile = '2.txt'
data = open(infile).read().strip()

def exec(isPart2):
    fileInfo = deque([])
    freeSpace = deque([])

    currentFileId = 0
    newDisk = []

    currentPosition = 0

    for index, parsedCurrentCharacter in enumerate(data):
        if index%2==0:                                          #gjore paren index ti e brojka, neparen .
            if isPart2:
                fileInfo.append((currentPosition, int(parsedCurrentCharacter), currentFileId))
            for j in range(int(parsedCurrentCharacter)):
                newDisk.append(currentFileId)
                if not isPart2:
                    fileInfo.append((currentPosition, 1, currentFileId))
                currentPosition += 1
            currentFileId += 1
        else:
            freeSpace.append((currentPosition, int(parsedCurrentCharacter)))
            for index in range(int(parsedCurrentCharacter)):
                newDisk.append(None)
                currentPosition += 1

    for (currentPosition, size, currentFileId) in reversed(fileInfo):
        for i,(spacePosition, spaceSize) in enumerate(freeSpace):
            if spacePosition < currentPosition and size <= spaceSize:
                for index in range(size):
                    newDisk[currentPosition+index] = None
                    newDisk[spacePosition+index] = currentFileId
                freeSpace[i] = (spacePosition + size, spaceSize-size)
                break

    returnMe = 0
    for index,parsedCurrentCharacter in enumerate(newDisk):
        if parsedCurrentCharacter is not None:
            returnMe += index*parsedCurrentCharacter
    return returnMe

part1 = exec(False)
part2 = exec(True)

print(part1)
print(part2)
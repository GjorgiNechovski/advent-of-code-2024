from collections import deque

DIRS = [(-1,0),(0,1),(1,0),(0,-1)]

infile = '1.txt'
data = open(infile).read().strip()

grid, moves = data.split('\n\n')
grid = grid.split('\n')

def solve(area, part2):
    rows = len(area)
    cols = len(area[0])
    area = [[area[r][c] for c in range(cols)] for r in range(rows)]

    if part2:
        scaledGrid = []
        for r in range(rows):
            row = []
            for c in range(cols):
                if area[r][c]== '#':
                    row.append('#')
                    row.append('#')
                if area[r][c]== 'O':
                    row.append('[')
                    row.append(']')
                if area[r][c]== '.':
                    row.append('.')
                    row.append('.')
                if area[r][c]== '@':
                    row.append('@')
                    row.append('.')
            scaledGrid.append(row)
        area = scaledGrid
        cols *= 2

    for r in range(rows):
        for c in range(cols):
            if area[r][c] == '@':
                startRow,startCol = r,c
                area[r][c] = '.'

    r,c = startRow,startCol
    for move in moves:
        if move == '\n':
            continue

        dirRow,dirCol = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<': (0,-1)}[move]
        curRow,curCol = r+dirRow,c+dirCol

        if area[curRow][curCol]== '#':
            continue
        elif area[curRow][curCol]== '.':
            r,c = curRow,curCol
        elif area[curRow][curCol] in ['[', ']', 'O']:
            queue = deque([(r,c)])
            visited = set()
            ok = True
            while queue:
                curRow,curCol = queue.popleft()
                if (curRow,curCol) in visited:
                    continue

                visited.add((curRow,curCol))
                nextRow,newCol = curRow+dirRow, curCol+dirCol
                if area[nextRow][newCol]== '#':
                    ok = False
                    break

                if area[nextRow][newCol] == 'O':
                    queue.append((nextRow,newCol))

                if area[nextRow][newCol]== '[':
                    queue.append((nextRow,newCol))
                    queue.append((nextRow,newCol+1))

                if area[nextRow][newCol]== ']':
                    queue.append((nextRow,newCol))
                    queue.append((nextRow,newCol-1))

            if not ok:
                continue

            while len(visited) > 0:
                for curRow,curCol in sorted(visited):
                    nextRow,newCol = curRow+dirRow,curCol+dirCol

                    if (nextRow,newCol) not in visited:
                        area[nextRow][newCol] = area[curRow][curCol]
                        area[curRow][curCol] = '.'
                        visited.remove((curRow,curCol))

            r = r+dirRow
            c = c+dirCol

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if area[r][c] in ['[', 'O']:
                ans += 100*r+c
    return ans

print(solve(grid, False))

print(solve(grid, True))
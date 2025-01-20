def find_constellations(r, c, n, grid):
    constellations = []
    
    def find_start(x, y):
        for cx in range(x, r):
            if grid[cx][y] == '*':
                return (cx, y)
        return None
    
    def mark_horizontal(x, y):
        for cy in range(y, c):
            if grid[x][cy] == '*':
                for cx in range(x, r):
                    if grid[cx][cy] == '*':
                        for cyy in range(cy, c):
                            if grid[x][cyy] == '*':
                                for cx in range(x, r):
                                    if grid[cx][cyy] == '*':
                                        constellations.append(((x, y), (cx, cyy)))
                                        return
            else:
                break
    
    def mark_vertical(x, y):
        for cx in range(x, r):
            if grid[cx][y] == '*':
                for cy in range(y, c):
                    if grid[cx][cy] == '*':
                        for cx in range(cx, r):
                            if grid[cx][y] == '*':
                                for cy in range(y, c):
                                    if grid[cx][cy] == '*':
                                        constellations.append(((x, y), (cx, cy)))
                                        return
            else:
                break
    
    for x in range(r):
        for y in range(c):
            if grid[x][y] == '*':
                mark_horizontal(x, y)
                mark_vertical(x, y)
    
    for cx in range(r):
        for cy in range(c):
            if grid[cx][cy] == '*':
                for nx, ny in constellations:
                    if (cx, cy) == nx or (cx, cy) == ny:
                        grid[cx][cy] = '+' if nx != (cx, cy) else '-'
                    elif cx == nx and cy == ny:
                        grid[cx][cy] = '+' if (nx, ny) != (cx, cy) else '|'
    
    for x in range(r):
        for y in range(c):
            if grid[x][y] == '*':
                print('*', end='')
            else:
                if grid[x][y] == '+':
                    print('+', end='')
                elif grid[x][y] == '-':
                    print('-', end='')
                else:
                    print('|', end='')
        print()

# Sample Input 1
r, c, n = 3, 3, 2
grid = [['*', '.', '*'], ['.', '*', '.'], ['*', '*', '*']]
find_constellations(r, c, n, grid)

# Sample Input 2
r, c, n = 6, 6, 3
grid = [['.', '.', '.', '*', '.', '.'], ['.', '.', '*', '.', '.', '.'], ['*', '.', '.', '*', '.', '.'], ['*', '.', '.', '.', '.', '*'], ['.', '.', '*', '.', '*', '.'], ['.', '.', '.', '*', '.', '.']]
find_constellations(r, c, n, grid)

# Sample Input 3
r, c, n = 11, 15, 8
grid = [['*', '.', '*', '.', '*', '.', '*', '.', '*', '.', '*', '.', '*', '.', '*'], ['.'] * 15, ['.' ] * 15 + ['*', '.', '*'], ['.'] * 15, ['*', '.', '*', '.', '*', '.', '*', '.', '*', '.', '*', '.', '*'], ['.'] * 15, ['*', '.', '*', '.', '*', '.', '*', '.', '*', '.', '*'], ['.'] * 15, ['*', '.' ] * 8 + ['*', '.', '*'], ['.'] * 15, ['*', '.', '*', '.', '*', '.', '*', '.', '*']]
find_constellations(r, c, n, grid)
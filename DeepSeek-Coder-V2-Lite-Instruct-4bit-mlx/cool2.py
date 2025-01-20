# Association for Cool Machineries (Part 1) solution input
N = 200
grid = [['A' for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if (i + j) % 2 == 0:
            grid[i][j] = 'C'
        else:
            grid[i][j] = 'D'
print(N)
for row in grid:
    print(''.join(row))
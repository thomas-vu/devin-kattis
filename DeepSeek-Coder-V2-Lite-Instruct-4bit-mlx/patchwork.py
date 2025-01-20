R, C = map(int, input().split())
grid = [['.' for _ in range(C)] for _ in range(R)]
N = int(input())
patches = []
for _ in range(N):
    ri, ci = map(int, input().split())
    patch = [input() for _ in range(ri)]
    patches.append(patch)
M = int(input())
for _ in range(M):
    qi, ti, pi = map(int, input().split())
    for i in range(len(patches[pi - 1])):
        for j in range(len(patches[pi - 1][i])):
            if patches[pi - 1][i][j] != '.':
                grid[qi + i][ti + j] = patches[pi - 1][i][j]
for row in grid:
    print(''.join(row))
H, L, K = map(int, input().split())
grid = [['_' for _ in range(L)] for __ in range(H)]

for i in range(K):
    l, h, a, b = map(int, input().split())
    for row in range(b, b + h):
        for col in range(a, a + l):
            grid[row][col] = chr(97 + i)  # 'a' is ASCII 97

for row in grid:
    print(''.join(row))
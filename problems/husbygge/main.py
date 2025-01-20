def solve(N, M, K, grid):
    houses = []
    for i in range(N):
        for j in range(M):
            houses.append((grid[i][j], i + 1, j + 1))
    houses.sort(reverse=True)
    
    chosen_houses = []
    for i in range(K):
        x, y = houses[i][1], houses[i][2]
        chosen_houses.append((x, y))
    return chosen_houses

# Read input
T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    result = solve(N, M, K, grid)
    for house in result:
        print(*house)
def max_min(N, grid):
    def check(mid):
        selected = set()
        for i in range(N):
            row = [grid[i][j] >= mid for j in range(N)]
            if True not in row:
                continue
            idx = row.index(True)
            if idx not in selected:
                selected.add(idx)
        return len(selected) == N
    
    left, right = 1, 10**6
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
print(max_min(N, grid))
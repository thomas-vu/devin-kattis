import sys
from itertools import permutations

# Read input
n, T = map(int, sys.stdin.readline().split())
tasks = []
for _ in range(n):
    pi, ti, di = map(int, sys.stdin.readline().split())
    tasks.append((pi, ti, di))

# Read travel times
travel_times = []
for _ in range(n + 2):
    travel_times.append(list(map(int, sys.stdin.readline().split())))

# Initialize DP and path arrays
dp = [[-1] * (T + 1) for _ in range(n + 1)]
path = [[[] for _ in range(T + 1)] for _ in range(n + 1)]
dp[0][0] = 0

# Fill DP table
for i in range(n + 1):
    for j in range(T + 1):
        if dp[i][j] != -1:
            for k in range(n):
                pi, ti, di = tasks[k]
                if j + ti <= T and (di == -1 or di <= j + ti):
                    if dp[i][j] + pi > dp[k + 1][j + ti]:
                        dp[k + 1][j + ti] = dp[i][j] + pi
                        path[k + 1][j + ti] = path[i][j] + [k + 1]

# Find the maximum points and corresponding tasks
max_points = max(dp[n + 1])
if max_points == 0:
    print()
else:
    for j in range(T + 1):
        if dp[n + 1][j] == max_points:
            tasks_to_perform = sorted(path[n + 1][j])
            print(max_points)
            print(' '.join(map(str, tasks_to_perform)))
            break
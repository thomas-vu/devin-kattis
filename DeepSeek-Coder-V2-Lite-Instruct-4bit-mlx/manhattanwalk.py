import sys
from math import inf
sys.setrecursionlimit(10**6)

def expected_waiting_time(r, c, p):
    # dp[i][j] will store the expected waiting time starting from cell (i, j)
    dp = [[-1.0 for _ in range(c)] for _ in range(r)]
    
    def dfs(x, y):
        if x == r - 1 and y == c - 1:
            return 0.0
        if dp[x][y] != -1.0:
            return dp[x][y]
        
        down_time = inf if x == r - 1 or (x + 1, y) in timers else dfs(x + 1, y)
        right_time = inf if y == c - 1 or (x, y + 1) in timers else dfs(x, y + 1)
        
        wait_time = (p + dfs(x, y)) / 2.0
        dp[x][y] = min(down_time, right_time, wait_time)
        return dp[x][y]
    
    global timers
    timers = set()
    
    def generate_timers(x, y, timer):
        if x == r - 1 and y == c - 1:
            return
        generate_timers(x + (1 if x < r - 1 else 0), y + (1 if y < c - 1 else 0), timer)
        timers.add((x, y))
    
    generate_timers(0, 0, p)
    return dfs(0, 0)

# Read input from stdin
r, c, p = map(int, sys.stdin.readline().strip().split())
result = expected_waiting_time(r, c, p)
print("{:.5f}".format(result))
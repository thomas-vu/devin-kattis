import sys
from math import sqrt, atan2, pi

def distance(spot1, spot2):
    return sqrt((spot1[0] - spot2[0])**2 + (spot1[1] - spot2[1])**2)

def calculate_sweat(path, spots):
    total_sweat = 0.0
    for i in range(len(path) - 1):
        start = spots[path[i]]
        end = spots[path[i + 1]]
        total_sweat += distance(start, end) * spots[path[i]][2]
    return total_sweat

def main():
    n = int(sys.stdin.readline().strip())
    spots = {}
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        spots[i] = (x, y, 0)  # x, y, sweat rate
    
    start = tuple(map(int, sys.stdin.readline().strip().split()))
    end = tuple(map(int, sys.stdin.readline().strip().split()))
    
    # Initialize sweat rates with initial rate r0
    for i in range(n):
        spots[i] = (spots[i][0], spots[i][1], spots[i][2])
    
    # Dynamic programming approach to find the minimum sweat path
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    path = [-1] * (n + 1)
    
    # Base case: starting from the dormitory to the first shady spot
    for i in range(n):
        dp[0][i] = distance(start, spots[i]) * spots[i][2]
    
    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(n):
            if i == 1 and j != 0:
                dp[i][j] = min(dp[i][j], distance(spots[0], spots[j]) * spots[j][2])
            for k in range(i):
                if j != k:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + distance(spots[k], spots[j]) * spots[j][2])
    
    # Reconstruct the path with minimum sweat
    min_sweat = float('inf')
    best_path = []
    
    for i in range(n):
        if dp[n][i] < min_sweat:
            min_sweat = dp[n][i]
            best_path = [i] + path[:i] + path[i+1:]
    
    # Output the best path or '-' if no shady spots are used
    if min_sweat == float('inf'):
        print('-')
    else:
        for p in best_path:
            if p != -1:
                print(p, end=' ')
        print()

if __name__ == "__main__":
    main()
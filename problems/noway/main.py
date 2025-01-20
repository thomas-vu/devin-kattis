MOD = 10**9 + 7

def add_mod(a, b):
    return (a + b) % MOD

def count_paths(R, C, roadworks):
    # Initialize the DP array with zeros
    dp = [[0] * C for _ in range(R)]
    dp[0][0] = 1
    
    # Mark the cells that are blocked by roadworks
    blocked = [[False] * C for _ in range(R)]
    for ri, mi in roadworks:
        for r in range(R):
            for c in range(C):
                if (r * C + c - ri) % mi == 0:
                    blocked[r][c] = True
    
    # Calculate the number of paths using dynamic programming
    for r in range(R):
        for c in range(C):
            if not blocked[r][c]:
                if r > 0 and not blocked[r - 1][c]:
                    dp[r][c] = add_mod(dp[r][c], dp[r - 1][c])
                if c > 0 and not blocked[r][c - 1]:
                    dp[r][c] = add_mod(dp[r][c], dp[r][c - 1])
    
    return dp[-1][-1]

def main():
    R, C, N = map(int, input().split())
    roadworks = [tuple(map(int, input().split())) for _ in range(N)]
    print(count_paths(R, C, roadworks))

if __name__ == "__main__":
    main()
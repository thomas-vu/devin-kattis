MOD = 10007

def knight_moves(H, W, rocks):
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    dp[1][1] = 1
    
    for r in range(1, H + 1):
        for c in range(1, W + 1):
            if (r, c) not in rocks:
                dp[r][c] += dp[r - 1][c] + dp[r][c - 1]
                dp[r][c] %= MOD
    
    return dp[H][W]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    results = []
    
    for case in range(1, N + 1):
        H = int(data[index])
        W = int(data[index + 1])
        R = int(data[index + 2])
        index += 3
        
        rocks = set()
        for _ in range(R):
            r = int(data[index])
            c = int(data[index + 1])
            rocks.add((r, c))
            index += 2
        
        result = knight_moves(H, W, rocks)
        results.append(f"Case #{case}: {result}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
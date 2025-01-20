def max_locations(city, W, H):
    # Initialize the DP table with -1 (unvisited)
    dp = [[-1] * W for _ in range(H)]
    
    # Starting point (0, 0) is walkable and interesting
    if city[0][0] == '.':
        dp[0][0] = 1 if city[0][0] == '*' else 0
    
    # First row and first column can only be reached by one direction
    for j in range(1, W):
        if city[0][j] == '.' and dp[0][j-1] != -1:
            dp[0][j] = dp[0][j-1] + 1 if city[0][j] == '*' else dp[0][j-1]
    for i in range(1, H):
        if city[i][0] == '.' and dp[i-1][0] != -1:
            dp[i][0] = dp[i-1][0] + 1 if city[i][0] == '*' else dp[i-1][0]
    
    # Fill the DP table for all other cells
    for i in range(1, H):
        for j in range(1, W):
            if city[i][j] == '.':
                top = dp[i-1][j] if city[i-1][j] == '.' else -1
                left = dp[i][j-1] if city[i][j-1] == '.' else -1
                if top != -1 or left != -1:
                    dp[i][j] = max(top, left) + 1 if city[i][j] == '*' else max(top, left)
    
    # The bottom-right corner contains the result
    return dp[-1][-1] if city[-1][-1] == '.' else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        W = int(data[index])
        H = int(data[index + 1])
        index += 2
        city = []
        for i in range(H):
            city.append(data[index + i])
        index += H
        result = max_locations(city, W, H)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
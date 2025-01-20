def min_army(R, C, map_, r, c):
    # Create a 2D list to store the minimum bannermen required for each cell
    dp = [[float('inf')] * C for _ in range(R)]
    
    # Base case: the castle position requires 0 bannermen to defend
    dp[r][c] = 0
    
    # Directions for moving up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Use dynamic programming to fill the dp table
    for i in range(r, -1, -1):
        for j in range(c, -1, -1):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + map_[i][j])
    
    for i in range(r, R):
        for j in range(c, C):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + map_[i][j])
    
    for i in range(r+1, R):
        for j in range(c+1, C):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + map_[i][j])
    
    for i in range(r+1, R):
        for j in range(c-1, -1, -1):
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + map_[i][j])
    
    # The minimum army required to defend the entire kingdom
    min_army = 0
    for i in range(R):
        for j in range(C):
            min_army += dp[i][j]
    
    return min_army

# Read input
R, C = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(R)]
r, c = map(int, input().split())

# Output the result
print(min_army(R, C, map_, r-1, c-1))
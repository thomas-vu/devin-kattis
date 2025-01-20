def min_cost_to_level_field(N, M, A, B, field):
    # Create a 2D array to store the minimum cost for each cell
    dp = [[float('inf') for _ in range(M)] for _ in range(N)]
    
    # Initialize the minimum cost based on the initial field configuration
    min_cost = float('inf')
    
    # Traverse the field to calculate the minimum cost for each cell
    for i in range(N):
        for j in range(M):
            # If the current patch is low ('.')
            if field[i][j] == '.':
                # If it's the first row, only consider coming from left or top-left
                if i == 0 and j == 0:
                    dp[i][j] = 0
                elif i == 0:
                    # Consider coming from left or top-left
                    dp[i][j] = min(dp[i][j], dp[i][j-1])
                elif j == 0:
                    # Consider coming from top or top-left
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
                else:
                    # Consider coming from left, top, or top-left
                    dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i][j-1])
                
                # If the current patch is low, no cost to change height
                if i > 0 and field[i-1][j] == '.':
                    dp[i][j] += 0
                else:
                    # Cost to move vertically if the previous patch is high
                    dp[i][j] += B
                
                # Cost to move horizontally if adjacent patches are different heights
                if j > 0 and field[i][j-1] != field[i][j]:
                    dp[i][j] += A
                
                # Update the minimum cost if it's lower than the current min_cost
                min_cost = min(min_cost, dp[i][j])
            else:  # If the current patch is high ('#')
                if i == 0 and j == 0:
                    dp[i][j] = B
                elif i == 0:
                    # Consider changing the height of this patch to be lower than the left one
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + B)
                elif j == 0:
                    # Consider changing the height of this patch to be lower than the top one
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + B)
                else:
                    # Consider changing the height of this patch to be lower than either left or top
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + B, dp[i][j-1] + B)
                
                # Cost to move horizontally if adjacent patches are different heights
                if j > 0 and field[i][j-1] != '#':
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + A)
                if i > 0 and field[i-1][j] != '#':
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + A)
                
                # Update the minimum cost if it's lower than the current min_cost
                min_cost = min(min_cost, dp[i][j])
    
    return min_cost

# Read input
N, M, A, B = map(int, input().split())
field = [input() for _ in range(N)]

# Calculate and output the minimum cost
print(min_cost_to_level_field(N, M, A, B, field))
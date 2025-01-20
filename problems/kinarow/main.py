def count_wins(games):
    hansel_wins = 0
    gretel_wins = 0
    
    for game in games:
        M, N, K = game['dimensions']
        grid = game['grid']
        
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 'x':
                    # Check horizontal
                    if col + K <= M and all(grid[row][col+i] == 'x' for i in range(K)):
                        hansel_wins += 1
                        break
                    # Check vertical
                    if row + K <= N and all(grid[row+i][col] == 'x' for i in range(K)):
                        hansel_wins += 1
                        break
                    # Check diagonal /
                    if col + K <= M and row + K <= N and all(grid[row+i][col+i] == 'x' for i in range(K)):
                        hansel_wins += 1
                        break
                    # Check diagonal \
                    if col - K < 0 and row + K <= N and all(grid[row+i][col-i] == 'x' for i in range(K)):
                        hansel_wins += 1
                        break
                elif grid[row][col] == 'o':
                    # Check horizontal
                    if col + K <= M and all(grid[row][col+i] == 'o' for i in range(K)):
                        gretel_wins += 1
                        break
                    # Check vertical
                    if row + K <= N and all(grid[row+i][col] == 'o' for i in range(K)):
                        gretel_wins += 1
                        break
                    # Check diagonal /
                    if col + K <= M and row + K <= N and all(grid[row+i][col+i] == 'o' for i in range(K)):
                        gretel_wins += 1
                        break
                    # Check diagonal \
                    if col - K < 0 and row + K <= N and all(grid[row+i][col-i] == 'o' for i in range(K)):
                        gretel_wins += 1
                        break
    
    return f"{hansel_wins}:{gretel_wins}"

# Read input
L = int(input())
games = []
for _ in range(L):
    M, N, K = map(int, input().split())
    grid = [input() for _ in range(N)]
    games.append({'dimensions': (M, N), 'grid': grid})

# Process and output the result
result = count_wins(games)
print(result)
def is_valid_tictactoe(grid):
    # Check rows, columns, and diagonals for a win condition
    lines = [grid[0:3], grid[3:6], grid[6:9],  # Rows
             [grid[0], grid[3], grid[6]],     # Cols
             [grid[1], grid[4], grid[7]],
             [grid[2], grid[5], grid[8]],
             [grid[0], grid[4], grid[8]],     # Diagonals
             [grid[2], grid[4], grid[6]]]
            ]
    
    # Count X's and O's
    count_x = sum(row.count('X') for row in lines)
    count_o = sum(row.count('O') for row in lines)
    
    # Check valid moves count
    if count_x < count_o or count_x > count_o + 1:
        return "no"
    
    # Count wins for X and O
    win_x = sum(line == ['X', 'X', 'X'] for line in lines)
    win_o = sum(line == ['O', 'O', 'O'] for line in lines)
    
    # Check win conditions
    if win_x and not win_o:
        return "yes" if count_x == count_o + 1 else "no"
    elif win_o and not win_x:
        return "yes" if count_x == count_o else "no"
    elif win_x and win_o:
        return "no"  # Both players cannot win
    else:
        return "yes"  # No wins, valid configuration

# Read input
N = int(input().strip())
for _ in range(N):
    grid = []
    for __ in range(3):
        row = input().strip()
        grid.extend([ch for ch in row])
    if _ < N - 1:
        input()  # Skip the empty line after each grid configuration except the last one
    print(is_valid_tictactoe(grid))
def min_draws(N, colors):
    # Initialize the position of the game piece
    position = 0
    draws = 0
    
    # Iterate through the board to determine the minimum number of draws needed
    while position < N:
        # Draw a card with the color of the current square
        current_color = colors[position]
        
        # Move to the nearest square with the same color
        for i in range(position + 1, N + 1):
            if i < N and colors[i] == current_color:
                position = i
            else:
                break
        
        # Increment the number of draws after each move
        draws += 1
    
    return draws

# Read input
N = int(input())
colors = [input().strip() for _ in range(N)]

# Output the result
print(min_draws(N, colors))
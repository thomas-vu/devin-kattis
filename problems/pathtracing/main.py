def draw_map(moves):
    # Initialize the map with all spaces and set start position to S
    min_x, max_x = 0, 0
    min_y, max_y = 0, 0
    pos_x, pos_y = 0, 0
    map_area = [[' ' for _ in range(51)] for _ in range(26)]
    map_area[pos_y][pos_x] = 'S'
    
    # Process each move
    for move in moves:
        if move == 'up':
            pos_y -= 1
        elif move == 'down':
            pos_y += 1
        elif move == 'left':
            pos_x -= 1
        elif move == 'right':
            pos_x += 1
        
        # Update min and max bounds
        if pos_x < min_x:
            min_x = pos_x
        elif pos_x > max_x:
            max_x = pos_x
        if pos_y < min_y:
            min_y = pos_y
        elif pos_y > max_y:
            max_y = pos_y
        
        # Mark the current position on the map
        map_area[pos_y][pos_x] = '*'
    
    # Mark the end position with E
    map_area[pos_y][pos_x] = 'E'
    
    # Draw the map outline and fill in spaces where no path was taken
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if map_area[y][x] == ' ':
                map_area[y][x] = ' '
    
    # Print the map outline and path
    print('#########')
    for y in range(min_y, max_y + 1):
        print('#', end='')
        for x in range(min_x, max_x + 1):
            print(map_area[y][x], end='')
        print('#')
    print('#########')

# Read moves from input until end of file
moves = []
while True:
    try:
        move = input()
        if move == 'end':
            break
        moves.append(move)
    except EOFError:
        break

# Draw the map based on the moves
draw_map(moves)
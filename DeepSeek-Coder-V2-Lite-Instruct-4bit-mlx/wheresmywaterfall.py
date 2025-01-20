def add_waterfall(map_, waterfalls, n, m):
    # Create a copy of the map to modify
    new_map = [list(row) for row in map_]
    
    # Add waterfalls to the top of each specified column
    for col in waterfalls:
        row = 0
        while row < n and map_[row][col] == 'O':
            new_map[row][col] = '~'
            row += 1
    
    # Propagate water to the right and left if obstructed
    for row in range(n):
        for col in range(m):
            if new_map[row][col] == '~':
                left = col - 1
                right = col + 1
                while left >= 0 and (new_map[row][left] == 'O' or new_map[row][left] == '?'):
                    new_map[row][left] = '~'
                    left -= 1
                while right < m and (new_map[row][right] == 'O' or new_map[row][right] == '?'):
                    new_map[row][right] = '~'
                    right += 1
    
    # Convert the modified map back to strings
    for i in range(n):
        new_map[i] = ''.join(new_map[i])
    
    return new_map

# Read input
n, m, k = map(int, input().split())
waterfalls = list(map(int, input().split()))
map_ = [input() for _ in range(n)]

# Add waterfalls to the map
updated_map = add_waterfall(map_, waterfalls, n, m)

# Output the updated map
for row in updated_map:
    print(row)
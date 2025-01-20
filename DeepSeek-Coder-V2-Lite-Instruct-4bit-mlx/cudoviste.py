def count_parking_spaces(R, C, city_map):
    parking_counts = [0] * 5
    
    for r in range(R):
        for c in range(C):
            if city_map[r][c] == '.':
                # Check for parking space of size 2x2
                if r + 1 < R and c + 1 < C:
                    if city_map[r + 1][c] == 'X' and city_map[r][c + 1] == 'X' and city_map[r + 1][c + 1] == 'X':
                        cars_to_squash = 0
                        if city_map[r + 1][c + 1] == 'X': cars_to_squash += 1
                        if city_map[r + 1][c] == 'X': cars_to_squash += 1
                        if city_map[r][c + 1] == 'X': cars_to_squash += 1
                        parking_counts[cars_to_squash] += 1
    
    return parking_counts

# Read input
R, C = map(int, input().split())
city_map = [input() for _ in range(R)]

# Calculate parking spaces
parking_counts = count_parking_spaces(R, C, city_map)

# Print output
for count in parking_counts:
    print(count)
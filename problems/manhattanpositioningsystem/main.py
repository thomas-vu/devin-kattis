def find_receiver_position(N, beacons):
    # Initialize lists to store possible positions for the receiver
    possible_positions = []
    
    # Iterate through all pairs of beacons to find potential receiver positions
    for i in range(N):
        for j in range(i+1, N):
            beacon1 = beacons[i]
            beacon2 = beacons[j]
            
            # Calculate potential receiver positions based on the Manhattan distance
            x1, y1, d1 = beacon1
            x2, y2, d2 = beacon2
            
            # Calculate the potential positions based on the distance to both beacons
            for dx in range(-d1, d1+1):
                x_pos = x1 + dx
                y_dist = d1 - abs(dx)
                
                # Check for potential positions on the Y-axis relative to beacon1
                if y_dist >= 0:
                    for dy in range(-y_dist, y_dist+1):
                        y_pos = y1 + dy
                        distance_sum = abs(x_pos - x2) + abs(y_pos - y2)
                        if distance_sum == d1 + d2:
                            possible_positions.append((x_pos, y_pos))
    
    # Check the number of possible positions
    if len(possible_positions) == 1:
        return f"{possible_positions[0][0]} {possible_positions[0][1]}"
    elif len(possible_positions) > 1:
        return "uncertain"
    else:
        return "impossible"

# Main function to read input and output the result
def main():
    N = int(input())
    beacons = [tuple(map(int, input().split())) for _ in range(N)]
    result = find_receiver_position(N, beacons)
    print(result)

if __name__ == "__main__":
    main()
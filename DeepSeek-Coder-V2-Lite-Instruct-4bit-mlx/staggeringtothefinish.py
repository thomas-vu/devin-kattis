import math

def calculate_starting_positions(N, R, S, W, F, L1, L2):
    # Calculate the outer radius of each lane
    R_outer = [R + (i * W) for i in range(N)]
    
    # Calculate the distance around each lane's semicircle
    arc_length = [math.pi * (R + (i * W)) for i in range(N)]
    
    # Calculate the total distance of each lane
    total_distance = [2 * S + arc_length[i] for i in range(N)]
    
    # Calculate the starting positions for each lane
    starting_positions = []
    for i in range(N):
        if i == 0:
            start_x = F - L1 * math.cos(math.atan2(W, S))
            start_y = -R - L1 * math.sin(math.atan2(W, S))
        else:
            start_x = F - (L1 + (i * L2)) * math.cos(math.atan2(W, S))
            start_y = -R - (L1 + (i * L2)) * math.sin(math.atan2(W, S))
        starting_positions.append((start_x, start_y))
    
    return starting_positions

# Read input
input_line = input().split()
N, R, S, W, F, L1, L2 = map(float, input_line)

# Process each race distance
while True:
    try:
        D = float(input())
        starting_positions = calculate_starting_positions(int(N), R, S, W, F, L1, L2)
        print("{:.3f}".format(D), end=' ')
        for position in starting_positions:
            print("{:.4f} {:.4f}".format(position[0], position[1]), end=' ')
        print()
    except EOFError:
        break
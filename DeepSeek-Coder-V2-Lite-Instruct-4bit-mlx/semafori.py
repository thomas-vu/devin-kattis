def calculate_time(N, L, traffic_lights):
    time = 0
    current_position = 0
    
    for D, R, G in traffic_lights:
        if current_position < D:
            time += (D - current_position)
            current_position = D
        while time % (R + G) < R:
            time += 1
        current_position = D + G
    
    if current_position < L:
        time += (L - current_position)
    
    return time

# Read input
N, L = map(int, input().split())
traffic_lights = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(calculate_time(N, L, traffic_lights))
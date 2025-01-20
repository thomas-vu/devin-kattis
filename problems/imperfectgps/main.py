import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def calculate_total_distance(positions):
    total_distance = 0.0
    for i in range(1, len(positions)):
        total_distance += calculate_distance(positions[i-1][0], positions[i-1][1], positions[i][0], positions[i][1])
    return total_distance

def calculate_gps_lost_percentage(positions, t):
    actual_total_distance = calculate_total_distance(positions)
    
    gps_distance = 0.0
    for i in range(1, len(positions)):
        gps_distance += calculate_distance(positions[i-1][0], positions[i-1][1], positions[i][0], positions[i][1])
    
    lost_distance = actual_total_distance - gps_distance
    percentage_lost = (lost_distance / actual_total_distance) * 100
    return percentage_lost

# Read input
n, t = map(int, input().split())
positions = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the result
percentage_lost = calculate_gps_lost_percentage(positions, t)
print("{:.8f}".format(percentage_lost))
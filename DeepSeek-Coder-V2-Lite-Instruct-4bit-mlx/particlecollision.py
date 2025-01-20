import math

# Function to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Function to check if a particle hits another
def check_collision(x1, y1, x2, y2, r):
    return distance(x1, y1, x2, y2) <= 2 * r

# Read input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
xv, yv, r = map(int, input().split())

# Check for different scenarios
if check_collision(x1, y1, x2, y2, r):
    if check_collision(x2, y2, x3, y3, r):
        print(1)  # Scenario where particle 1 hits particle 2 which then hits particle 3
    else:
        print(2)  # Scenario where particle 1 hits particle 2 and particle 2 moves indefinitely
elif check_collision(x1, y1, x3, y3, r):
    if check_collision(x3, y3, x2, y2, r):
        print(1)  # Scenario where particle 1 hits particle 3 which then hits particle 2
    else:
        print(4)  # Scenario where particle 1 hits particle 3 and particle 3 moves indefinitely
else:
    print(5)  # Scenario where particle 1 moves indefinitely
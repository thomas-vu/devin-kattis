def shortest_distance(n1, n2):
    # Calculate the difference in degrees
    diff = (n2 - n1) % 360
    # If the difference is more than 180 degrees, take the shorter path
    if diff > 180:
        diff -= 360
    return diff

# Read input
n1 = int(input())
n2 = int(input())

# Calculate the shortest distance and output the result
result = shortest_distance(n1, n2)
print(result)
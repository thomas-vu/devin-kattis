def can_reach(a, b, c, d, t):
    # Calculate the Manhattan distance between start and end points
    manhattan_distance = abs(a - c) + abs(b - d)
    
    # Check if the remaining charge can cover the Manhattan distance
    return (t - manhattan_distance) % 2 == 0 and t >= manhattan_distance

# Read input from stdin
a, b = map(int, input().split())
c, d = map(int, input().split())
t = int(input())

# Determine if it's possible to reach the destination with the given charge
result = can_reach(a, b, c, d, t)
print("Y" if result else "N")
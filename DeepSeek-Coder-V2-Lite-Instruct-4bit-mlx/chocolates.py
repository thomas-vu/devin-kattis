def count_polygons(R, C):
    if R == 1 and C == 1:
        return 1
    elif R == 1 or C == 1:
        n = max(R, C)
        return (n * (n + 1)) // 2
    else:
        # For R, C >= 2
        return (R * (R + 1) // 2) * (C * (C + 1) // 2)

# Read input
R, C = map(int, input().split())

# Calculate and print the result
print(count_polygons(R, C))
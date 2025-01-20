def max_birds(l, d, n, positions):
    if n == 0:
        # If no birds are already sitting, we can place them at least d from poles and n*d between each other
        return (l - 12) // (d - 6) + 1
    else:
        positions.sort()
        max_additional = 0
        for i in range(n):
            left = positions[i] - d if i == 0 else max(positions[i] - d, positions[i-1] + d)
            right = l - (positions[-1] - d if i == n-1 else min(positions[i] + d, positions[i+1] - d))
            additional = (right - left) // d - 1
            max_additional += additional
        return max_additional

# Read input
l, d, n = map(int, input().split())
positions = [int(input()) for _ in range(n)]

# Calculate and output the result
print(max_birds(l, d, n, positions))
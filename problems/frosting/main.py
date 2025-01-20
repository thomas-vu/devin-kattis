def count_areas(n, A, B):
    areas = [0, 0, 0]
    for i in range(n):
        for j in range(n):
            color = (i + j) % 3
            areas[color] += A[i] * B[j]
    return areas

# Read input
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Calculate areas for each color
areas = count_areas(n, A, B)

# Output the result
print(*areas)
def calculate_qaly(N, periods):
    total_qaly = 0.0
    for q, y in periods:
        total_qaly += q * y
    return total_qaly

# Read input
N = int(input())
periods = [tuple(map(float, input().split())) for _ in range(N)]

# Calculate and output the result
result = calculate_qaly(N, periods)
print("{:.3f}".format(result))
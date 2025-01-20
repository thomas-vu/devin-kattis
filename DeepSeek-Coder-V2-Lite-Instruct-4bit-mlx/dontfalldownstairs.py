def calculate_minimum_effort(N, steps):
    effort = 0
    for i in range(1, N):
        if steps[i] > steps[i - 1]:
            effort += steps[i] - steps[i - 1]
    return effort

# Read input
N = int(input())
steps = list(map(int, input().split()))

# Calculate and print the minimum effort
E = calculate_minimum_effort(N, steps)
print(E)
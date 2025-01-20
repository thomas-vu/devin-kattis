def min_washing_machines(S, C, K, colors):
    colors.sort()
    machines = 0
    i = 0
    while i < S:
        machine_color = colors[i]
        j = i + 1
        while j < S and colors[j] <= machine_color + K:
            j += 1
        machines += 1
        i = j
    return machines

# Read input
S, C, K = map(int, input().split())
colors = list(map(int, input().split()))

# Output the result
print(min_washing_machines(S, C, K, colors))
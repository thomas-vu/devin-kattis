def possible_distance(D, steps):
    for i in range(len(steps) - 1):
        for j in range(i + 1, len(steps)):
            if (steps[j] - steps[i]) / (j - i) == D:
                return "possible"
    return "impossible"

D, N = map(float, input().split())
steps = list(map(int, input().split()))
print(possible_distance(D, steps))
import sys
P = float(sys.stdin.readline().strip())
weights = [1, 2, 3, 4, 5]
counts = [0] * 5
total_weight = sum(weights)
target = P * total_weight / (total_weight - 5)
for i in range(len(weights)):
    while sum([a * b for a, b in zip(counts, weights)]) + weights[i] <= target:
        counts[i] += 1
answer = [str(count) for count in counts]
print(' '.join(answer))
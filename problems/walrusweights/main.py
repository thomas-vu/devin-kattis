n = int(input())
plates = [int(input()) for _ in range(n)]
best_weight = 0
min_diff = float('inf')

for i in range(n):
    for j in range(i+1, n):
        total_weight = plates[i] + plates[j]
        diff = abs(1000 - total_weight)
        if diff < min_diff:
            min_diff = diff
            best_weight = total_weight
        elif diff == min_diff and total_weight > best_weight:
            best_weight = total_weight

print(best_weight)
def min_additional_results(N, P, scores):
    current_sum = sum(scores)
    target_sum = P * (N + x)
    if target_sum > current_sum + 100 * x:
        return "impossible"
    else:
        return x

# Read input
N, P = map(int, input().split())
scores = list(map(int, input().split()))

# Calculate the minimum number of additional results needed
result = min_additional_results(N, P, scores)
print(result)
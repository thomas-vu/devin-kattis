def candy_bags(t, test_cases):
    results = []
    for case in test_cases:
        K, C = case
        needed = (K * X) + 1
        if needed > 10**9:
            results.append("IMPOSSIBLE")
        else:
            bags = (needed + C - 1) // C
            results.append(bags)
    return results

# Read input
t = int(input().strip())
test_cases = [tuple(map(int, input().strip().split())) for _ in range(t)]

# Process and output results
results = candy_bags(t, test_cases)
for result in results:
    print(result)
def expected_attempts(passwords):
    probabilities = [p for _, p in passwords]
    cumulative_probabilities = list(reversed([sum(probabilities[i:]) for i in range(len(passwords))]))
    expected_value = sum([(i + 1) * p for i, p in enumerate(cumulative_probabilities)])
    return expected_value

# Read input
N = int(input().strip())
passwords = []
for _ in range(N):
    password, probability = input().strip().split()
    probabilities.append((float(probability)))
passwords = list(zip(sorted(passwords, key=lambda x: float(x[1]), reverse=True), cumulative_probabilities))

# Calculate and output the expected number of attempts
print("{:.4f}".format(expected_attempts(passwords)))
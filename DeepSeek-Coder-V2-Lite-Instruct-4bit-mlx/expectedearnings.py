def should_play(n, k, p):
    expected_loss = (1 - p) * n - p * k
    return "spela" if expected_loss < 0 else "spela inte!"

# Read input
n, k = map(int, input().split())
p = float(input())

# Output the result
print(should_play(n, k, p))
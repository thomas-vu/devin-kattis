N = int(input())
cards = list(map(int, input().split()))
Q = int(input())
queries = [list(map(int, input().split())) for _ in range(Q)]

# Create a frequency array to count occurrences of each card number
freq = [0] * (10**9 + 2)
for card in cards:
    freq[card] += 1

# Prefix sum array to quickly calculate the number of cards in a range
prefix_sum = [0] * (10**9 + 2)
for i in range(1, 10**9 + 2):
    prefix_sum[i] = freq[i] + prefix_sum[i - 1]

# Process each query
for l, r in queries:
    result = prefix_sum[r] - prefix_sum[l - 1]
    print(result)
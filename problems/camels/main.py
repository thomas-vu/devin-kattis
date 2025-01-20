# Read input
n = int(input())
jaap_bets = list(map(int, input().split()))
jan_bets = list(map(int, input().split()))
thijs_bets = list(map(int, input().split()))

# Initialize counts for each camel
counts = [0] * (n + 1)

# Count the number of times each camel appears in the same position across all bets
for i in range(n):
    for j in range(n):
        if jaap_bets[i] == jan_bets[j] and jaap_bets[i] == thijs_bets[j]:
            counts[jaap_bets[i]] += 1

# Calculate the number of pairs where all three bets have the same order
pairs = sum(counts[i] * (counts[i] - 1) // 2 for i in range(1, n + 1))

# Output the result
print(pairs)
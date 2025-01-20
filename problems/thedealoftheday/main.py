from math import comb

def ways_to_deal(cards):
    total = sum(cards)
    if total < K:
        return 0
    
    ways = 1
    for i in range(10):
        if cards[i] > 0:
            ways *= comb(cards[i], min(K - sum(cards[:i]), cards[i]))
    return ways

# Read input
import sys
input = sys.stdin.read
data = input().split()

# Process data
cards = list(map(int, data[0].split()))
K = int(data[1])

# Calculate and print the result
result = ways_to_deal(cards)
print(result)
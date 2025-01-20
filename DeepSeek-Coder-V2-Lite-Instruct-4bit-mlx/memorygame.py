def count_pairs(N, K, cards):
    card_count = {}
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    pairs = 0
    for count in card_count.values():
        pairs += count // 2
    
    return pairs

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
K = int(data[1])
cards = list(map(int, data[2:]))

# Output the result
print(count_pairs(N, K, cards))
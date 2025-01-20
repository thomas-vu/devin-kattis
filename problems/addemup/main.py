def can_win(n, s, cards):
    seen = set()
    for card in cards:
        if (s - card) in seen:
            return "YES"
        seen.add(card)
    return "NO"

# Read input
n, s = map(int, input().split())
cards = list(map(int, input().split()))

# Check if a pair of cards can add up to the sum s
result = can_win(n, s, cards)
print(result)
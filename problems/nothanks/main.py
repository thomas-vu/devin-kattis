def calculate_score(cards):
    score = 0
    i = 0
    while i < len(cards):
        if i + 1 < len(cards) and cards[i] + 1 == cards[i + 1]:
            # Skip consecutive numbers
            while i + 1 < len(cards) and cards[i] + 1 == cards[i + 1]:
                i += 1
        else:
            score += cards[i]
        i += 1
    return score

# Read input
n = int(input())
cards = list(map(int, input().split()))

# Calculate and output the score
print(calculate_score(cards))
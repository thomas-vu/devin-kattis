def min_turns(N, cards):
    card_count = {}
    for card in cards:
        if card not in card_count:
            card_count[card] = 0
        card_count[card] += 1
    
    straight_lengths = []
    for card in sorted(card_count.keys()):
        if card_count[card] > 0:
            count = 0
            for i in range(card, card + 5):
                if i in card_count:
                    count += card_count[i]
            straight_lengths.append(count)
    
    return N - max(straight_lengths)

# Read input
N = int(input())
cards = list(map(int, input().split()))

# Output the result
print(min_turns(N, cards))
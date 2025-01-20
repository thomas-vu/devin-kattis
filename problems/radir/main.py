def can_form_sequence(cards):
    values = [0] * 14
    for card in cards:
        value = card[1]
        values[value] += 1
    
    for i in range(1, 14):
        if values[i] >= 1 and values[i+1] >= 1 and values[i+2] >= 1:
            return True
    return False

def min_turns_to_sequence(n, p, cards):
    initial_cards = cards[:p]
    remaining_cards = cards[p:]
    
    min_turns = float('inf')
    for mask in range(1 << (n - p)):
        hand = initial_cards.copy()
        turns = 0
        for i in range(n - p):
            if (mask >> i) & 1:
                hand.append(remaining_cards[i])
                turns += 1
        
        if can_form_sequence(hand):
            min_turns = min(min_turns, turns)
    
    return min_turns if min_turns != float('inf') else "Neibb"

# Read input
n, p = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = min_turns_to_sequence(n, p, cards)
print(result)
def strength_of_hand(cards):
    ranks = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}
    rank_counts = [0] * 14
    
    for card in cards:
        rank = card[:-1]
        rank_counts[ranks[rank]] += 1
    
    return max(rank_counts)

cards = input().split()
print(strength_of_hand(cards))
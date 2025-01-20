def card_value(card):
    rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return rank[card]

def max_cards_won(opponent_pile, yraglac_pile):
    opponent_values = [card_value(card) for card in opponent_pile]
    yraglac_values = [card_value(card) for card in yraglac_pile]
    
    # Sort both piles in descending order of card values
    opponent_values.sort(reverse=True)
    yraglac_values.sort(reverse=True)
    
    # Use a greedy approach to maximize the number of cards won
    wins = 0
    i, j = 0, 0
    while i < len(opponent_values) and j < len(yraglac_values):
        if yraglac_values[j] > opponent_values[i]:
            wins += 1
            i += 1
        j += 1
    
    return wins

# Read number of games
N = int(input())
for _ in range(N):
    opponent_pile = input()
    yraglac_pile = input()
    
    # Calculate and print the maximum number of cards Yraglac can win
    result = max_cards_won(opponent_pile, yraglac_pile)
    print(result)
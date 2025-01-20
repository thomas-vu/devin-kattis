def can_win_after_reshuffle(hands):
    if len(hands) == 0:
        return "impossible"
    
    # Separate the cards by suits
    clubs = []
    diamonds = []
    hearts = []
    spades = []
    
    for card in hands:
        rank, suit = card.split()
        rank = int(rank)
        if suit == 'C':
            clubs.append(rank)
        elif suit == 'D':
            diamonds.append(rank)
        elif suit == 'H':
            hearts.append(rank)
        else:
            spades.append(rank)
    
    # Sort the cards in each suit
    clubs.sort()
    diamonds.sort()
    hearts.sort()
    spades.sort()
    
    # Check if it's possible to win after reshuffling
    def can_win(hand):
        if len(hand) < 7:
            return False
        for i in range(len(hand) - 5):
            if hand[i] == 1 and all(rank > 1 for rank in hand[i+1:]):
                return True
        return False
    
    if can_win(clubs) and can_win(diamonds) and can_win(hearts) and can_win(spades):
        return "possible"
    else:
        return "impossible"

# Read the number of cards in the hand
n = int(input())
hands = [input().strip() for _ in range(n)]
print(can_win_after_reshuffle(hands))
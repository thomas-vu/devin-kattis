def min_moves_to_sort(cards):
    card_order = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    sorted_cards = sorted(cards, key=lambda x: (card_order[x[0]], x[1]))
    
    def count_moves(cards, sorted_cards):
        n = len(cards)
        pos = {card: i for i, card in enumerate(cards)}
        moves = 0
        for i in range(n):
            target_index = pos[sorted_cards[i]]
            while i < target_index:
                next_card = cards[i + 1]
                current_pos = pos[cards[i]]
                next_pos = pos[next_card]
                if current_pos < next_pos:
                    cards[i], cards[i + 1] = cards[i + 1], cards[i]
                    pos[cards[i]], pos[cards[i + 1]] = i, i + 1
                else:
                    cards[i], cards[next_pos] = next_card, cards[i]
                    pos[cards[i]], pos[next_card] = next_pos, i
                moves += 1
                i += 1
            while i > target_index:
                next_card = cards[i - 1]
                current_pos = pos[cards[i]]
                prev_pos = pos[next_card]
                if current_pos > prev_pos:
                    cards[i], cards[i - 1] = next_card, cards[i]
                    pos[cards[i]], pos[next_card] = prev_pos, i
                else:
                    cards[i], cards[i - 1] = cards[i - 1], next_card
                    pos[cards[i]], pos[cards[i - 1]] = i - 1, i
                moves += 1
                i -= 1
        return moves
    
    original_moves = count_moves(list(cards), sorted_cards)
    reversed_moves = count_moves([cards[i] for i in range(len(cards) - 1, -1, -1)], [sorted_cards[i] for i in range(len(sorted_cards) - 1, -1, -1)])
    return min(original_moves, reversed_moves)

# Read input
n = int(input().strip())
cards = [input().strip() for _ in range(n)]

# Output the minimum number of moves required to sort the hand
print(min_moves_to_sort(cards))
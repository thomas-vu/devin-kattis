def min_remaining_cards(n, cards):
    stack = []
    for card in cards:
        if len(stack) > 0 and (stack[-1] + card) % 2 == 0:
            stack.pop()
        else:
            stack.append(card)
    return len(stack)

# Read input
n = int(input())
cards = list(map(int, input().split()))

# Output the result
print(min_remaining_cards(n, cards))
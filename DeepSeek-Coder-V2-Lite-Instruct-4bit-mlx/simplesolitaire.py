def remove_cards(hand):
    stack = []
    for card in hand:
        while len(stack) >= 2 and ((card[0] == stack[-1][0] or card[1] == stack[-2][0]) or (card[0] == stack[-2][0] or card[1] == stack[-1][0])):
            if (card[0] == stack[-1][0] or card[1] == stack[-2][0]) and (card[0] == stack[-2][0] or card[1] == stack[-1][0]):
                stack.pop()
                stack.pop()
            else:
                stack.pop()
        stack.append(card)
    return stack

def main():
    hands = [input().split() for _ in range(4)]
    hand_index = 0
    while True:
        removed = False
        for i in range(len(hands[hand_index])):
            card = hands[hand_index][i]
            for j in range(3):
                if hand_index > 0 and i - j - 1 >= 0:
                    prev_card = hands[hand_index - 1][i - j - 1]
                    if (card[0] == prev_card[0] or card[1] == prev_card[1]):
                        removed = True
                        hands[hand_index - 1].pop(i - j - 1)
                        hands[hand_index].pop(i)
                        break
            if removed:
                break
        hand_index += 1
        if hand_index == 4:
            break
    remaining = []
    for hand in hands:
        remaining.extend(hand)
    print(len(remaining), end=' ')
    for card in remaining:
        print(card, end=' ')

main()
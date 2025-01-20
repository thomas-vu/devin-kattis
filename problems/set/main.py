def check_set(cards):
    for attr in ['number', 'shape', 'color', 'fill']:
        values = [getattr(card, attr) for card in cards]
        if not (len(set(values)) == 1 or len(set(values)) == 3):
            return False
    return True

class Card:
    def __init__(self, card_str):
        self.number = int(card_str[0])
        self.shape = card_str[1]
        self.color = card_str[2]
        self.fill = card_str[3]

    def __repr__(self):
        return f"{self.number}{self.shape}{self.color}{self.fill}"

cards = []
for _ in range(4):
    line = input().split()
    for card_str in line:
        cards.append(Card(card_str))

sets = []
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            if check_set([cards[i], cards[j], cards[k]]):
                set_card_numbers = [cards[i].number, cards[j].number, cards[k].number]
                set_card_numbers.sort()
                sets.append(f"{set_card_numbers[0]} {set_card_numbers[1]} {set_card_numbers[2]}")

if sets:
    for set in sets:
        print(set)
else:
    print("no sets")
def main():
    N, dominant_suit = input().split()
    N = int(N)
    points = 0
    card_values = {
        'A': (11, 11),
        'K': (4, 4),
        'Q': (3, 3),
        'J': (20, 2),
        'T': (10, 10),
        '9': (14, 0),
        '8': (0, 0),
        '7': (0, 0)
    }
    
    for _ in range(4 * N):
        card, suit = input().split()
        value, dominant_value = card_values[card]
        if suit == dominant_suit:
            points += value
        else:
            points += dominant_value
    
    print(points)

if __name__ == "__main__":
    main()
def can_play_all_cards(hands):
    from collections import defaultdict
    
    picture_count = defaultdict(int)
    
    for card in hands:
        p, q = card
        picture_count[p] += 1
        picture_count[q] += 1
    
    for count in picture_count.values():
        if count % 2 != 0:
            return "impossible"
    return "possible"

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        n = int(input())
        hands = [tuple(map(int, input().split())) for _ in range(n)]
        results.append(can_play_all_cards(hands))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
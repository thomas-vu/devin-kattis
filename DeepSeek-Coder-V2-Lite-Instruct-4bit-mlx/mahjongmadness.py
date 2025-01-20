def expected_value(x, hand):
    from itertools import combinations
    
    def is_winning_hand(tiles):
        counts = [0] * 10
        for tile in tiles:
            counts[tile] += 1
        
        # Check pairs and sets
        for i in range(1, 10):
            if counts[i] == 2:
                counts[i] = 0
            elif counts[i] >= 3:
                counts[i] -= 3
        
        for i in range(1, 8):
            while counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
                counts[i] -= 1
                counts[i+1] -= 1
                counts[i+2] -= 1
        
        return sum(counts) == 0
    
    total_combinations = 0
    winning_combinations = 0
    
    for discard in range(14):
        new_hand = hand[:]
        new_hand[discard] = x
        for draw in range(1, 10):
            if draw not in new_hand:
                temp_hand = new_hand[:]
                temp_hand[discard] = draw
                if is_winning_hand(temp_hand):
                    winning_combinations += 1
                total_combinations += 1
    
    return winning_combinations / total_combinations if total_combinations > 0 else 0

def main():
    x = int(input())
    hand = list(map(int, input().split()))
    result = expected_value(x, hand)
    print("{:.6f}".format(result))

if __name__ == "__main__":
    main()
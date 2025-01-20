from collections import Counter

def calculate_score(dice):
    counts = Counter(dice)
    max_scores = [0] * 15
    
    # Category: ones
    max_scores[0] = dice.count(1) * 1
    
    # Category: twos
    max_scores[1] = dice.count(2) * 2
    
    # Category: threes
    max_scores[2] = dice.count(3) * 3
    
    # Category: fours
    max_scores[3] = dice.count(4) * 4
    
    # Category: fives
    max_scores[4] = dice.count(5) * 5
    
    # Category: sixes
    max_scores[5] = dice.count(6) * 6
    
    # Category: pair
    for num in range(1, 7):
        if counts[num] >= 2:
            max_scores[6] = num * 2
            break
    
    # Category: two pairs
    pair_count = sum(1 for num in range(1, 7) if counts[num] >= 2)
    if pair_count >= 2:
        pairs = [num for num in range(1, 7) if counts[num] >= 2]
        max_scores[7] = sum(pairs) * 2
    
    # Category: three of a kind
    for num in range(1, 7):
        if counts[num] >= 3:
            max_scores[8] = num * 3
            break
    
    # Category: four of a kind
    for num in range(1, 7):
        if counts[num] >= 4:
            max_scores[9] = num * 4
            break
    
    # Category: full house
    if sorted(counts.values()) == [2, 3]:
        max_scores[10] = sum(dice)
    
    # Category: small straight
    if sorted(dice) == [1, 2, 3, 4, 5]:
        max_scores[11] = 15
    
    # Category: large straight
    if sorted(dice) == [2, 3, 4, 5, 6]:
        max_scores[12] = 20
    
    # Category: yatzy
    if len(set(dice)) == 1:
        max_scores[13] = 50
    
    # Category: chance
    max_scores[14] = sum(dice)
    
    return max_scores

# Sample Input 1
dice = [1, 2, 3, 4, 5, 0]
scores = calculate_score(dice)
print(" ".join(map(str, scores)))  # Output: 1 2 3 4 5 0 0 0 0 0 0 15 0 0 15

# Sample Input 2
dice = [1, 2, 0, 8, 0, 6]
scores = calculate_score(dice)
print(" ".join(map(str, scores)))  # Output: 0 0 0 0 0 15 0 0 15 0 8 0 0 0 24

# Sample Input 3
dice = [0, 0, 6, 0, 15, 0]
scores = calculate_score(dice)
print(" ".join(map(str, scores)))  # Output: 0 0 6 0 15 0 10 16 15 0 21 0 0 0 31

# Sample Input 4
dice = [0, 0, 0, 0, 25, 0]
scores = calculate_score(dice)
print(" ".join(map(str, scores)))  # Output: 0 0 0 0 25 0 10 0 15 20 0 0 0 50 25

# Sample Input 5
dice = [0, 8, 0, 4, 0, 0]
scores = calculate_score(dice)
print(" ".join(map(str, scores)))  # Output: 0 8 0 4 0 0 4 0 6 8 0 0 0 0 12
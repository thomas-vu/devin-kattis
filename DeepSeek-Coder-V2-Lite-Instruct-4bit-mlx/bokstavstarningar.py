def count_valid_words(N, K, dice_sides, wordlist):
    from itertools import product
    
    # Generate all possible combinations of dice sides
    possible_combinations = list(product(*dice_sides))
    
    # Count the number of valid words that can be constructed
    count = 0
    for combination in possible_combinations:
        word = ''.join(combination)
        if word in wordlist:
            count += 1
    
    return count

# Read input
N, K, M = map(int, input().split())
dice_sides = [input().strip() for _ in range(N)]
wordlist = [input().strip() for _ in range(M)]

# Count and print the number of valid words
print(count_valid_words(N, K, dice_sides, wordlist))
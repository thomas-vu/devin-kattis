def generate_spoilers(words):
    from itertools import product
    
    # Generate all possible combinations of the words
    word_combinations = list(product(*words))
    
    # Convert each combination into a string and sort them
    spoilers = [(' '.join(combo)) for combo in word_combinations]
    spoilers.sort()
    
    return spoilers

# Read input
n = int(input())
words = []
for _ in range(n):
    line = input().strip()
    parts = list(map(str.strip, line.split()))
    k = int(parts[0])
    word_options = parts[1:]
    words.append(word_options)

# Generate and print spoilers
spoilers = generate_spoilers(words)
for spoiler in spoilers:
    print(spoiler)
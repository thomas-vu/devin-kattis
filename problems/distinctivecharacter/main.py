n, k = map(int, input().split())
characters = [input() for _ in range(n)]

# Initialize the list to store the count of each feature's presence in characters
feature_count = [0] * k

# Count the number of times each feature is present in all characters
for character in characters:
    for i, bit in enumerate(character):
        if bit == '1':
            feature_count[i] += 1

# Determine the features for Tira's character to minimize maximum similarity
tira_character = ''
min_max_similarity = float('inf')
for mask in range(2**k):
    # Convert the mask to a binary string of k bits
    tira_binary = bin(mask)[2:].zfill(k)
    
    # Calculate the maximum similarity with any character
    max_similarity = 0
    for character in characters:
        similarity = sum(1 for i, bit in enumerate(character) if tira_binary[i] == bit)
        max_similarity = max(max_similarity, similarity)
    
    # Update the minimum maximum similarity and Tira's character if needed
    if max_similarity < min_max_similarity:
        min_max_similarity = max_similarity
        tira_character = tira_binary

# Output Tira's character
print(tira_character)
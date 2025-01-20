# Read input
S = input()
M = input()

# Split the memo into words
words = M.split()

# Iterate over each word in the memo
for i, word in enumerate(words):
    # Check if any character in the word is a forbidden letter
    for char in word:
        if char in S:
            # Replace all occurrences of the forbidden letter with '*'
            words[i] = word.replace(char, '*')

# Join the modified words back into a single string
result = ' '.join(words)

# Output the result
print(result)
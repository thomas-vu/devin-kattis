n = int(input())
languages = list(map(int, input().split()))

# Create a dictionary to store the first and last occurrence of each language
language_positions = {}

# Initialize min_awkwardness to a large number
min_awkwardness = float('inf')

# Iterate through the seating arrangement to find the minimum awkwardness level
for i in range(n):
    if languages[i] not in language_positions:
        # If the language is encountered for the first time, record its position
        language_positions[languages[i]] = i
    else:
        # If the language has been seen before, calculate the distance to its last occurrence
        min_awkwardness = min(min_awkwardness, i - language_positions[languages[i]])
        # Update the position of this language to the current index
        language_positions[languages[i]] = i

# Output the minimum awkwardness level found
print(min_awkwardness)
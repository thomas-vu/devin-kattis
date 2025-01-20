def count_vowels(word):
    vowels_not_y = set('aeiou')
    count1 = sum(1 for char in word if char in vowels_not_y)
    count2 = sum(1 for char in word if char in 'aeiouy')
    return count1, count2

# Read input from stdin
word = input().strip()

# Get the counts
count1, count2 = count_vowels(word)

# Print the result
print(count1, count2)
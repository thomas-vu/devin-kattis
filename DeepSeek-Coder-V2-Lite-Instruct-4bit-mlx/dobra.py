def is_pleasant(word):
    vowels = 'AEIOU'
    for i in range(len(word) - 2):
        if word[i] in vowels and word[i+1] in vowels and word[i+2] in vowels:
            return False
        if not word[i] in vowels and not word[i+1] in vowels and not word[i+2] in vowels:
            return False
    if 'L' not in word:
        return False
    return True

def count_pleasant_words(s):
    words = s.split('_')
    count = 0
    for word in words:
        if is_pleasant(word):
            count += 1
    return count

# Read input
s = input().strip()

# Output the result
print(count_pleasant_words(s))
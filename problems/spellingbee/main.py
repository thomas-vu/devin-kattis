def find_words(center, letters, words):
    def is_valid(word):
        if len(word) < 4:
            return False
        for char in word:
            if char not in letters or char == center and word.count(char) > 1:
                return False
        return True
    
    valid_words = [word for word in words if is_valid(word)]
    return sorted(valid_words)

# Read input
center = input().strip()
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# Find and output the matching words
matching_words = find_words(center, set([center] + list(input().strip())), words)
for word in matching_words:
    print(word)
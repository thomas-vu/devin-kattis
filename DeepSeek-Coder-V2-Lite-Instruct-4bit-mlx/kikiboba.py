def categorize_word(word):
    b_count = word.count('b')
    k_count = word.count('k')
    
    if b_count == 0 and k_count == 0:
        return "none"
    elif b_count > k_count:
        return "boba"
    elif k_count > b_count:
        return "kiki"
    else:
        return "boki"

# Read input from stdin
word = input().strip()

# Categorize the word and print the result
category = categorize_word(word)
print(category)
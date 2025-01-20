def find_original_word(s):
    n = len(s)
    # Each word is repeated three times with possibly one mistyped letter
    word_length = n // 3
    
    # Check each position to see if it's the same as the others
    for i in range(word_length):
        if s[i] != s[i + word_length] or s[i] != s[i + 2 * word_length]:
            # Find the position where the mistype is
            for j in range(3 * word_length):
                if s[j] != s[i]:
                    # Replace the mistyped letter with the correct one
                    corrected_s = s[:j] + s[i] + s[j+1:]
                    break
            return find_original_word(corrected_s)
    # If no mistype found, the word is the repeated part
    return s[:word_length]

# Read input from stdin
s = input().strip()
print(find_original_word(s))
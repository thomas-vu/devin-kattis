def has_repeated_words(phrase):
    words = phrase.split()
    seen_words = set()
    
    for word in words:
        if word in seen_words:
            return "no"
        seen_words.add(word)
    
    return "yes"

# Read input from stdin
import sys
input_line = sys.stdin.readline().strip()

# Output the result
print(has_repeated_words(input_line))
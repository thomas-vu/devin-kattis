def reverse_words(word):
    n = len(word)
    best_word = word
    
    for i in range(1, n):
        for j in range(i+1, n):
            w1 = word[:i]
            w2 = word[i:j]
            w3 = word[j:]
            
            reversed_w1 = w1[::-1]
            reversed_w2 = w2[::-1]
            reversed_w3 = w3[::-1]
            
            candidate = reversed_w1 + reversed_w2 + reversed_w3
            if candidate < best_word:
                best_word = candidate
    
    return best_word

# Read input from stdin
word = input().strip()

# Output the best word
print(reverse_words(word))
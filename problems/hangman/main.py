def hangman(word, permutation):
    guessed_letters = set()
    
    for letter in permutation:
        if letter in word and letter not in guessed_letters:
            guessed_letters.add(letter)
        if set(word).issubset(guessed_letters):
            return "WIN"
    
    return "LOSE"

# Read input from stdin
word = input().strip()
permutation = input().strip()

# Output the result
print(hangman(word, permutation))
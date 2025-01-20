def find_word_and_last_player(P, M):
    words = ["Efficiency", "Unbreaking", "Silk", "Touch"]
    
    # Calculate the total number of turns for each word in one round
    turns_per_word = 4 * P
    
    # Determine the word at the M-th turn
    index = (M - 1) % turns_per_word
    
    # Determine the word being said at the M-th turn
    if index < P:
        word = "Efficiency"
    elif index < 2 * P:
        word = "Unbreaking"
    elif index < 3 * P:
        word = "Silk"
    else:
        word = "Touch"
    
    # Determine the last player to say a word in this round
    last_player = (M - 1) % P + 1
    
    return word, last_player

# Read input from the user
P = int(input())
M = int(input())

# Get the word and last player
word, last_player = find_word_and_last_player(P, M)

# Print the output
print(word)
print(last_player)
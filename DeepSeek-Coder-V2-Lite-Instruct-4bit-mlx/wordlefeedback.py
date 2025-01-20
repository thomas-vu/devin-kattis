def wordle_feedback(secret, guess):
    result = ''
    secret_count = {char: 0 for char in set(secret)}
    guess_count = {char: 0 for char in set(guess)}
    
    # Count occurrences of each character in the secret word and the guess
    for char in secret:
        secret_count[char] += 1
    for char in guess:
        guess_count[char] += 1
    
    # Determine the feedback for each letter in the guess
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            result += 'G'
            secret_count[guess[i]] -= 1
            guess_count[guess[i]] -= 1
        else:
            result += '-'
    
    # Determine the feedback for letters that are in the guess but not at the correct position
    for i in range(len(guess)):
        if guess[i] != secret[i]:
            if guess_count[guess[i]] > 0 and secret_count[guess[i]] > 0:
                result = result[:i] + 'Y' + result[i+1:]
                secret_count[guess[i]] -= 1
            guess_count[guess[i]] -= 1
    
    return result

# Read input
secret = input().strip()
guess = input().strip()

# Get the feedback and print it
feedback = wordle_feedback(secret, guess)
print(feedback)
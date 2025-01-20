import sys

def get_feedback(guess, secret):
    feedback = ""
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            feedback += 'O'
        elif guess[i] in secret:
            feedback += '/'
        else:
            feedback += 'X'
    return feedback

def main():
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    
    while True:
        guess = words[0]  # Start with the first word in the list
        print(guess)
        sys.stdout.flush()
        
        feedback = input().strip()
        if feedback == 'OOOOO':
            break
        
        # Remove the guessed word and update the list based on feedback
        words = [word for word in words if get_feedback(word, guess) == feedback]

if __name__ == "__main__":
    main()
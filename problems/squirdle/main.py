import sys
from string import ascii_lowercase

def generate_guess(current_guess, feedback):
    for i in range(5):
        if feedback[i] == '1':
            # Replace a character in the guess to match the position
            for char in ascii_lowercase:
                if char not in current_guess:
                    current_guess[i] = char
                    break
        elif feedback[i] == '2':
            # Keep the character in the position
            continue
        elif feedback[i] == '0':
            # Remove characters not in the word
            current_guess = [c for c in current_guess if c != current_guess[i]]
    return ''.join(current_guess)

def main():
    current_guess = list('a' * 5)
    for _ in range(10):
        guess = ''.join(current_guess)
        print(f"?{guess}")
        sys.stdout.flush()
        feedback = input().strip()
        if feedback == '22222':
            break
        current_guess = list(generate_guess(current_guess, feedback))

if __name__ == "__main__":
    main()
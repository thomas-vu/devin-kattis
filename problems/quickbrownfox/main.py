def find_missing_letters(phrase):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    phrase_letters = {char.lower() for char in phrase if char.isalpha()}
    missing_letters = letters - phrase_letters
    return ''.join(sorted(missing_letters)) if missing_letters else None

def main():
    N = int(input())
    for _ in range(N):
        phrase = input()
        missing_letters = find_missing_letters(phrase)
        if missing_letters:
            print('missing', missing_letters)
        else:
            print('pangram')

if __name__ == "__main__":
    main()
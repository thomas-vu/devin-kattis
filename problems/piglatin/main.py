def pig_latin_word(word):
    vowels = 'aeiou'
    if word[0] in vowels:
        return word + 'yay'
    else:
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + 'ay'
        return word  # This should not happen as per the problem statement

def main():
    while True:
        try:
            line = input()
            words = line.split()
            pig_latin_words = [pig_latin_word(word) for word in words]
            print(' '.join(pig_latin_words))
        except EOFError:
            break

if __name__ == "__main__":
    main()
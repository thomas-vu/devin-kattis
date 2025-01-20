def nearest_hard_consonant(c):
    hard_consonants = 'bcdfgnkpqt'
    min_diff = float('inf')
    nearest_char = ''
    for hc in hard_consonants:
        diff = abs(ord(hc) - ord(c))
        if diff < min_diff:
            min_diff = diff
            nearest_char = hc
        elif diff == min_diff and ord(hc) < ord(nearest_char):
            nearest_char = hc
    return nearest_char

def convert_word(word):
    if not word:
        return ''
    
    hard_consonants = 'bcdfgnkpqt'
    word = word.lower()
    
    # First letter conversion
    first_letter = nearest_hard_consonant(word[0])
    
    # Replace hard consonants in subsequent syllables
    new_word = first_letter + word[1:]
    for i in range(1, len(new_word)):
        if new_word[i] in hard_consonants:
            new_word = new_word[:i] + first_letter + new_word[i+1:]
    
    # Remove trailing hard consonant if present
    while new_word and new_word[-1] in hard_consonants:
        new_word = new_word[:-1]
    
    # Add appropriate ending
    if new_word:
        last_char = nearest_hard_consonant(new_word[-1])
        if last_char == 'b':
            new_word += 'ah'
        elif last_char == 'c':
            new_word += 'oh'
        else:
            new_word += 'uh'
    
    return new_word.capitalize()

def convert_sentence(sentence):
    words = sentence.split(' ')
    converted_words = [convert_word(word) for word in words]
    return ' '.join(converted_words)

# Read input from standard input
sentence = input().strip()
print(convert_sentence(sentence))
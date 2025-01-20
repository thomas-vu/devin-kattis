def soundex(word):
    # Define the Soundex mapping for digits to letters
    soundex_map = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    
    # Convert the first letter of the word to uppercase
    word = word.upper()
    
    # Replace each letter with its Soundex digit
    soundex_code = word[0]
    for letter in word[1:]:
        if letter.isalpha():
            soundex_code += soundex_map.get(letter, '')
    
    # Remove consecutive duplicates and ensure the code is 4 characters long
    soundex_code = ''.join(soundex_code[i] for i in range(len(soundex_code)) if i == 0 or soundex_code[i] != soundex_code[i - 1])
    soundex_code = (soundex_code + '0' * (4 - len(soundex_code)))[:4]
    
    return soundex_code

# Read input lines and process each line to produce Soundex code
import sys
for word in sys.stdin:
    word = word.strip()
    print(soundex(word))
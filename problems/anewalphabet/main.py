# Python solution for New Alphabet problem

def translate_char(c):
    translations = {
        'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3',
        'f': '#', 'g': '6', 'h': '[-]', 'i': '|', 'j': '_|',
        'k': '|<', 'l': '1', 'm': '[]\/[]', 'n': '[]\[]',
        'o': '0', 'p': '|D', 'q': '(,)', 'r': '|Z',
        's': '$', 't': '']['', 'u': '|_|', 'v': '\/',
        'w': '\/\/', 'x': '{}', 'y': '`\/', 'z': '2',
        'A': '@', 'B': '8', 'C': '(', 'D': '|)', 'E': '3',
        'F': '#', 'G': '6', 'H': '[-]', 'I': '|', 'J': '_|',
        'K': '|<', 'L': '1', 'M': '[]\/[]', 'N': '[]\[]',
        'O': '0', 'P': '|D', 'Q': '(,)', 'R': '|Z',
        'S': '$', 'T': '']['', 'U': '|_|', 'V': '\/',
        'W': '\/\/', 'X': '{}', 'Y': '`\/', 'Z': '2'
    }
    return translations.get(c, c)

def translate_text(text):
    translated = ""
    for char in text:
        translated += translate_char(char)
    return translated

# Read input
input_text = input().strip()

# Translate and output the result
translated_text = translate_text(input_text)
print(translated_text)
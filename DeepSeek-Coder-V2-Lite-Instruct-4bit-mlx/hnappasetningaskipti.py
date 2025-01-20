def convert_keyboard(type1, type2, text):
    # Create dictionaries to map keys from type1 to type2 and vice versa
    mapping = {
        'qwerty': {
            'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't',
            'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p',
            'a': 'a', 's': 's', 'd': 'd', 'f': 'f', 'g': 'g',
            'h': 'h', 'j': 'j', 'k': 'k', 'l': 'l', 'z': 'z',
            'x': 'x', 'c': 'c', 'v': 'v', 'b': 'b', 'n': 'n',
            'm': 'm', ',': ',', '.': '.', '/': '/'
        },
        'dvorak': {
            'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't',
            'y': 'y', 'u': 'u', 'i': 'i', 'o': 'o', 'p': 'p',
            'a': 'b', 's': 's', 'd': 'n', 'f': 'v', 'g': 'k',
            'h': 'm', 'j': 'f', 'k': 'u', 'l': 'g', 'z': 'c',
            'x': 'm', 'c': 'w', 'v': 'j', 'b': 'd', 'n': 'i',
            'm': 't', ',': '/', '.': ';', '/': ','
        },
        'bjarki': {
            'q': 'q', 'w': 'w', 'e': 'e', 'r': 'r', 't': 't',
            'y': 'y', 'u': 'u', 'i': 'o', 'o': 'p', 'p': 'a',
            'a': 'q', 's': 'w', 'd': 'e', 'f': 'r', 'g': 't',
            'h': 'y', 'j': 'u', 'k': 'i', 'l': 'o', 'z': 'j',
            'x': 'k', 'c': 'x', 'v': 'z', 'b': 'c', 'n': 'v',
            'm': 'b', ',': 'l', '.': ';', '/': ','
        }
    }
    
    # Determine the mapping based on the keyboard layouts
    if type1 == 'qwerty' and type2 == 'qwerty':
        map_func = lambda x: mapping['qwerty'][x] if x in mapping['qwerty'] else x
    elif type1 == 'dvorak' and type2 == 'dvorak':
        map_func = lambda x: mapping['dvorak'][x] if x in mapping['dvorak'] else x
    elif type1 == 'bjarki' and type2 == 'bjarki':
        map_func = lambda x: mapping['bjarki'][x] if x in mapping['bjarki'] else x
    elif type1 == 'qwerty' and type2 == 'dvorak':
        map_func = lambda x: mapping['qwerty'][x] if x in mapping['qwerty'] else (mapping['dvorak'][x] if x in mapping['dvorak'] else x)
    elif type1 == 'qwerty' and type2 == 'bjarki':
        map_func = lambda x: mapping['qwerty'][x] if x in mapping['qwerty'] else (mapping['bjarki'][x] if x in mapping['bjarki'] else x)
    elif type1 == 'dvorak' and type2 == 'qwerty':
        map_func = lambda x: mapping['dvorak'][x] if x in mapping['dvorak'] else (mapping['qwerty'][x] if x in mapping['qwerty'] else x)
    elif type1 == 'dvorak' and type2 == 'bjarki':
        map_func = lambda x: mapping['dvorak'][x] if x in mapping['dvorak'] else (mapping['bjarki'][x] if x in mapping['bjarki'] else x)
    elif type1 == 'bjarki' and type2 == 'qwerty':
        map_func = lambda x: mapping['bjarki'][x] if x in mapping['bjarki'] else (mapping['qwerty'][x] if x in mapping['qwerty'] else x)
    elif type1 == 'bjarki' and type2 == 'dvorak':
        map_func = lambda x: mapping['bjarki'][x] if x in mapping['bjarki'] else (mapping['dvorak'][x] if x in mapping['dvorak'] else x)
    
    # Convert the text using the determined mapping
    converted_text = ''.join(map_func(char) for char in text)
    return converted_text

# Read input from stdin
import sys
input = sys.stdin.read
data = input().splitlines()

# Process each line of the input
for line in data:
    type1, _, type2 = line.split()
    text = input().strip()
    converted_text = convert_keyboard(type1, type2, text)
    print(converted_text)
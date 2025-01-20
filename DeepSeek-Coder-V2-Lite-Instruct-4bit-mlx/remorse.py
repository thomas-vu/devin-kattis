def morse_code_length(s):
    # Define the Morse code equivalents for each letter (ignoring case)
    morse_dict = {
        'A': '.',
        'B': '---',
        'C': '..-',
        'D': '--.',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '.',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..'
    }
    
    # Remove non-letter characters
    s = ''.join(filter(str.isalpha, s))
    
    # Initialize the minimum length to a large number
    min_length = float('inf')
    
    # Try all possible assignments of Morse code sequences to letters in the string
    for i in range(1 << len(morse_dict)):
        code = ''
        length = 0
        for char in s:
            morse_code = morse_dict[char.upper()] if char.isalpha() else ''
            code += morse_code + ' ' * (i & 1)
            length += len(morse_code) + (1 if i & 1 else 0)
            i >>= 1
        # Adjust for the final space character at the end of each character's Morse code
        min_length = min(min_length, length - 1)
    
    return min_length

# Read input from stdin
s = input().strip()
print(morse_code_length(s))
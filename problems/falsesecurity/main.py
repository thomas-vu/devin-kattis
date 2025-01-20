def decode_message(encoded_message):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '_': '..--', '.': '---.', ',': '.-.-', '?': '----'
    }
    
    morse_to_char = {value: key for key, value in morse_code.items()}
    
    encoded_message = encoded_message.replace('  ', ' * ')
    parts = encoded_message.split()
    
    lengths = []
    current_length = 0
    for part in parts:
        if part == '*':
            lengths.append(current_length)
            current_length = 0
        else:
            morse_code_str = ''.join(part.split('*'))
            lengths.append(len(morse_code_str))
            current_length += len(morse_code_str)
    
    lengths.reverse()
    
    decoded_message = ''
    index = 0
    for length in lengths:
        morse_code_str = parts[index][:length]
        decoded_message += morse_to_char[morse_code_str]
        index += 1
    
    return decoded_message

# Read input from stdin
import sys
for line in sys.stdin:
    decoded_message = decode_message(line.strip())
    print(decoded_message)
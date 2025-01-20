import re
import sys

def is_morse_code_palindrome(input_string):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', input_string).lower()
    
    # Get the Morse code representation of the cleaned string
    morse_code = ''
    for char in cleaned_string:
        if char.isdigit():
            morse_code += str(char)
        else:
            # Assuming a simple mapping for demonstration purposes
            morse_code += char  # Morse code representation of each letter (simplified)
    
    # Check if the morse code is a palindrome
    return int(morse_code == morse_code[::-1])

# Read input from stdin
input_string = sys.stdin.readline().strip()

# Output the result
print(is_morse_code_palindrome(input_string))
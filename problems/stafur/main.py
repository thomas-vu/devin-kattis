def determine_letter(letter):
    vowels = "AEIOU"
    if letter in vowels:
        return "Jebb"
    elif letter == 'Y':
        return "Kannski"
    else:
        return "Neibb"

# Read the input from stdin
letter = input().strip()

# Determine and print the result
print(determine_letter(letter.upper()))
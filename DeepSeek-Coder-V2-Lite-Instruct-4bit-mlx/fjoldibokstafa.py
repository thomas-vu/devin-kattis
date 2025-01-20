import sys

def count_letters(input_str):
    return sum(1 for char in input_str if char.isalpha())

# Read from standard input
input_line = sys.stdin.readline().strip()

# Count the letters in the input string
letter_count = count_letters(input_line)

# Output the result
sys.stdout.write(str(letter_count) + '\n')
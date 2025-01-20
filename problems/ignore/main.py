def upside_down_digits(num):
    # Mapping of digits when viewed upside down
    upside_down_map = {
        '0': '0',
        '1': '1',
        '2': '5',
        '3': '3',
        '4': '3',
        '5': '2',
        '6': '9',
        '7': '3',
        '8': '8',
        '9': '6'
    }
    
    # Convert the number to a string, then map each digit and reverse it
    upside_down_num = ''.join(upside_down_map[digit] for digit in str(num))
    return upside_down_num[::-1]

# Function to generate valid numbers
def generate_valid_numbers(max_digits):
    valid_numbers = []
    i = 1
    while len(valid_numbers) < max_digits:
        upside_down = upside_down_digits(i)
        if str(i) == upside_down:  # Ensure the number is valid when viewed normally
            valid_numbers.append(str(i))
        i += 1
    return valid_numbers

# Generate a list of valid numbers up to the maximum needed
valid_numbers = generate_valid_numbers(1100)

# Read input from stdin
import sys
input_lines = [line.strip() for line in sys.stdin if line.strip()]

# Output the corresponding valid number for each input K_i
for k in input_lines:
    print(valid_numbers[int(k) - 1])
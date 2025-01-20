def swap_digits(code):
    # Convert the code to a list of characters for easy swapping
    digits = [char for char in code]
    # Swap the two digits
    swapped_digits = [digits[1], digits[0]]
    # Join the swapped digits back into a string and return
    return ''.join(swapped_digits)

# Read input from stdin
input_code = input().strip()
# Get the swapped code and print it
swapped_code = swap_digits(input_code)
print(swapped_code)
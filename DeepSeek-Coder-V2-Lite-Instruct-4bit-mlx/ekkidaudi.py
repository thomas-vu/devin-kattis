def convert_to_horizontal(input_lines):
    top, bottom = input_lines
    index = top.index('|')
    left = top[:index]
    right = bottom[index:]
    return left + right

# Read input from stdin
input_lines = [input().strip() for _ in range(2)]

# Process the input and output the result
output = convert_to_horizontal(input_lines)
print(output)
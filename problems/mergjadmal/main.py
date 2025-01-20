def process_input(input_str):
    if '69' in input_str or '420' in input_str:
        return "Mergjad!"
    else:
        return "Leim!"

# Read the input from stdin
input_str = input().strip()

# Process and output the result
print(process_input(input_str))
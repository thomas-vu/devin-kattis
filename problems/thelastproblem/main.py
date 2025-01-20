def generate_farewell(name):
    return f"Thank you, {name}, and farewell!"

# Read input from standard input
input_string = input().strip()

# Generate and print the farewell message
print(generate_farewell(input_string))
def generate_response(s):
    return 'h' + s[1:].replace('e', 'ee')

# Read input from stdin
s = input().strip()

# Output the response
print(generate_response(s))
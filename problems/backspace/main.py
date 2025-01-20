def correct_string(s):
    stack = []
    for char in s:
        if char == '<':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Read input from stdin
s = input().strip()
# Print the corrected string
print(correct_string(s))
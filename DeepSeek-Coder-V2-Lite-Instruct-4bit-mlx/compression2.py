def compress_string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

# Read input from stdin
s = input().strip()

# Output the result of running DRY on the input string
print(compress_string(s))
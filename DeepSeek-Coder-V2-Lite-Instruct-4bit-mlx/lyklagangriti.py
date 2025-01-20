def decode_password(keys):
    password = []
    stack = []
    
    for key in keys:
        if key == 'L':
            stack.append(password.pop())
        elif key == 'R':
            if password:
                stack.append(password.pop())
        elif key == 'B':
            if stack:
                password.append(stack.pop())
        else:
            password.append(key)
    
    return ''.join(password + list(reversed(stack)))

# Read input from stdin
keys = input().strip()

# Output the decoded password
print(decode_password(keys))
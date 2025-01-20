def remove_explosions(s, explosion):
    stack = []
    explosion_length = len(explosion)
    
    for char in s:
        if char == explosion[-1] and ''.join(stack[-explosion_length:]) == explosion[:-1]:
            for _ in range(explosion_length - 1):
                stack.pop()
        else:
            stack.append(char)
    
    result = ''.join(stack)
    return result if result else "FRULA"

# Read input
s = input().strip()
explosion = input().strip()

# Process and output the result
print(remove_explosions(s, explosion))
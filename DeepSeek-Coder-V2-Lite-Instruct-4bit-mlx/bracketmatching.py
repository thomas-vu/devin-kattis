def is_valid_bracket_sequence(s):
    stack = []
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for bracket in s:
        if bracket in "([{":
            stack.append(bracket)
        elif bracket in ")]}":
            if not stack or stack[-1] != matching_bracket[bracket]:
                return "Invalid"
            stack.pop()
    
    return "Valid" if not stack else "Invalid"

# Read input
n = int(input())
s = input()

# Check the bracket sequence and output the result
print(is_valid_bracket_sequence(s))
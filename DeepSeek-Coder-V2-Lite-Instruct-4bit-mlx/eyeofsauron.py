def check_tower(s):
    left_bars = 0
    right_bars = s.count('|')
    
    if right_bars < 2:
        return "fix"
    
    for i in range(len(s)):
        if s[i] == '|':
            left_bars += 1
        elif s[i] == ')':
            if right_bars - left_bars == 1:
                return "correct"
            else:
                return "fix"
        elif s[i] == '(':
            if left_bars - right_bars == 1:
                return "correct"
            else:
                return "fix"
    return "fix"

# Read input from stdin
s = input().strip()

# Check the tower and print the result
print(check_tower(s))
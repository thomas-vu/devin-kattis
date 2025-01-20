import re

def is_valid_constant(line):
    # Check for decimal constant
    if re.fullmatch(r'\d+', line):
        return True
    
    # Check for base with digits pattern
    if re.fullmatch(r'\d+#[\da-fA-F]+#', line):
        base, digits = re.match(r'(\d+)\#([\da-fA-F]+)\#', line).groups()
        base = int(base)
        if 2 <= base <= 16 and all(('0' <= c <= '9') or ('a' <= c.lower() <= 'f') for c in digits):
            return True
    
    return False

n = int(input())
for _ in range(n):
    line = input()
    print("yes" if is_valid_constant(line) else "no")
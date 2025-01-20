def is_wff(s):
    stack = []
    for char in s:
        if char in 'pqt':
            stack.append(char)
        elif char == 'N':
            if len(stack) < 1:
                return False
            stack.append('N' + stack.pop())
        elif char in 'KANC':
            if len(stack) < 2:
                return False
            x = stack.pop()
            w = stack.pop()
            if char == 'K':
                stack.append('K' + w + x)
            elif char == 'A':
                stack.append('A' + w + x)
            elif char == 'N':
                stack.append('N' + w)
            elif char == 'C':
                stack.append('C' + w + x)
    return len(stack) == 1 and isinstance(stack[0], str)

def longest_wff(s):
    symbols = 'pqrst'
    max_length = 0
    best_wff = None
    
    for mask in range(1, 2**len(s)):
        subset = ''.join([s[i] for i in range(len(s)) if (mask & (1 << i))])
        if is_wff(subset):
            if len(subset) > max_length:
                max_length = len(subset)
                best_wff = subset
    
    if max_length == 0:
        return "no WFF possible"
    else:
        return best_wff

while True:
    s = input()
    if s == '0':
        break
    print(longest_wff(s))
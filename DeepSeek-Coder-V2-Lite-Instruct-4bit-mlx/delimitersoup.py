def find_mismatch(line):
    stack = []
    for i, char in enumerate(line):
        if char in '([{':
            stack.append((char, i))
        elif char in ')]}':
            if not stack:
                return char, i
            top_char, top_index = stack.pop()
            if (top_char == '(' and char != ')') or \
               (top_char == '[' and char != ']') or \
               (top_char == '{' and char != '}') :
                return char, i
    if stack:
        _, index = stack.pop()
        return None, index
    return 'ok so far'

# Read input
import sys
input = sys.stdin.read
line = input().split('\n')
length_L = int(line[0])
program = line[1]

result = find_mismatch(program)
if result == 'ok so far':
    print('ok so far')
else:
    char, index = result if result else ('', -1)
    print(char, index)
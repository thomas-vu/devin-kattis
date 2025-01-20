MOD = 10**9 + 7

def evaluate_bracket_sequence(tokens):
    stack = []
    for token in tokens:
        if token == '(':
            stack.append(token)
        elif token == ')':
            value = 0
            while stack and isinstance(stack[-1], int):
                value += stack.pop()
            while stack and stack[-1] == '(':
                stack.pop()
                break
            while stack and isinstance(stack[-1], int):
                mid = stack.pop()
                left = stack.pop() if stack[-1] == '(' else 0
                right = stack.pop() if stack[-1] == '(' else stack.pop()
                value *= (left + right)
                stack.append(value % MOD)
            else:
                value = value % MOD
        elif isinstance(token, int):
            stack.append(token)
    return sum(stack) % MOD

# Read input
n = int(input())
tokens = list(map(str, input().split()))

# Evaluate and print the result
result = evaluate_bracket_sequence(tokens)
print(result)
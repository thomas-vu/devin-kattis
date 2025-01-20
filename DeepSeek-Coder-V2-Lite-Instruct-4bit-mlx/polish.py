def evaluate(expression):
    stack = []
    for token in reversed(expression.split()):
        if token in "+-*":
            a = stack.pop()
            b = stack.pop()
            if isinstance(a, int) and isinstance(b, int):
                result = a + b if token == '+' else a - b if token == '-' else a * b
                stack.append(result)
            else:
                stack.extend([a, b, token])
        else:
            stack.append(int(token) if token[-1].isdigit() else token)
    while len(stack) > 1:
        b = stack.pop()
        a = stack.pop()
        operator = stack.pop()
        if isinstance(a, int) and isinstance(b, int):
            result = a + b if operator == '+' else a - b if operator == '-' else a * b
            stack.append(result)
        else:
            stack.extend([a, b, operator])
    return stack[0] if stack else []

def simplify_expression(expression):
    tokens = expression.split()
    simplified = []
    for token in reversed(tokens):
        if token in "+-*":
            left = simplified.pop()
            right = simplified.pop()
            if isinstance(left, int) and isinstance(right, int):
                left_val = left
                right_val = right
            else:
                simplified.extend([left, right, token])
                continue
            if isinstance(right, int) and not left.isalpha():
                left_val = evaluate([left])[0]
            elif isinstance(left, int) and not right.isalpha():
                right_val = evaluate([right])[0]
            simplified.append(left_val + right_val if token == '+' else left_val - right_val if token == '-' else left_val * right_val)
        else:
            simplified.append(int(token) if token[-1].isdigit() else token)
    while len(simplified) > 1:
        right = simplified.pop()
        left = simplified.pop()
        operator = simplified.pop()
        if isinstance(left, int) and isinstance(right, int):
            left_val = left
            right_val = right
        else:
            simplified.extend([left, right, operator])
            continue
        if isinstance(right, int) and not left.isalpha():
            left_val = evaluate([left])[0]
        elif isinstance(left, int) and not right.isalpha():
            right_val = evaluate([right])[0]
        simplified.append(left_val + right_val if operator == '+' else left_val - right_val if operator == '-' else left_val * right_val)
    return simplified[0] if simplified else []

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    for i, line in enumerate(data):
        simplified_expr = simplify_expression(line)
        if isinstance(simplified_expr, int):
            simplified_expr = [str(simplified_expr)]
        print("Case {}: {}".format(i + 1, ' '.join(simplified_expr)))

if __name__ == "__main__":
    main()
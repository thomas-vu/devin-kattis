def evaluate_expression(a, b, c, d, op1, op2):
    if op1 == '+':
        if op2 == '+':
            return (a + b) == (c + d)
        elif op2 == '-':
            return (a + b) == (c - d)
        elif op2 == '*':
            return (a + b) == (c * d)
        elif op2 == '/':
            if d != 0 and (c % d) == 0:
                return (a + b) == (c // d)
            else:
                return False
    elif op1 == '-':
        if op2 == '+':
            return (a - b) == (c + d)
        elif op2 == '-':
            return (a - b) == (c - d)
        elif op2 == '*':
            return (a - b) == (c * d)
        elif op2 == '/':
            if d != 0 and (c % d) == 0:
                return (a - b) == (c // d)
            else:
                return False
    elif op1 == '*':
        if op2 == '+':
            return (a * b) == (c + d)
        elif op2 == '-':
            return (a * b) == (c - d)
        elif op2 == '*':
            return (a * b) == (c * d)
        elif op2 == '/':
            if d != 0 and (c % d) == 0:
                return (a * b) == (c // d)
            else:
                return False
    elif op1 == '/':
        if op2 == '+':
            return (a // b) == (c + d)
        elif op2 == '-':
            return (a // b) == (c - d)
        elif op2 == '*':
            return (a // b) == (c * d)
        elif op2 == '/':
            if d != 0 and (c % d) == 0:
                return (a // b) == (c // d)
            else:
                return False
    return False

def generate_expressions(a, b, c, d):
    operators = ['+', '-', '*', '/']
    valid_expressions = []
    
    for op1 in operators:
        for op2 in operators:
            if evaluate_expression(a, b, c, d, op1, op2):
                expr = f"{a} {op1} {b} = {c} {op2} {d}"
                valid_expressions.append(expr)
    
    return valid_expressions

a, b, c, d = map(int, input().split())
valid_expressions = generate_expressions(a, b, c, d)
if valid_expressions:
    for expr in sorted(valid_expressions):
        print(expr)
else:
    print("problems ahead")
import sys
import re

def evaluate_expression(expr):
    # Remove spaces from the expression
    expr = expr.replace(' ', '')
    
    # Handle multiplication and division first
    while True:
        match = re.search(r'\d+\.?\d*([*/])\d+\.?\d*', expr)
        if not match:
            break
        left, op, right = match.group(1), match.start(), match.end()
        left_val = float(expr[:left]) if '.' in expr[:left] else int(expr[:left])
        right_val = float(expr[left+1:right]) if '.' in expr[left+1:right] else int(expr[left+1:right])
        if op == '*':
            new_val = left_val * right_val
        else:
            new_val = left_val / right_val
        expr = str(new_val) + expr[right:]
    
    # Now handle addition and subtraction
    while True:
        match = re.search(r'[\+\-]\d+\.?\d*', expr)
        if not match:
            break
        op, right = match.group(0)[0], match.end()
        left_val = float(expr[:right-1]) if '.' in expr[:right-1] else int(expr[:right-1])
        right_val = float(expr[right:]) if '.' in expr[right:] else int(expr[right:])
        if op == '+':
            new_val = left_val + right_val
        else:
            new_val = left_val - right_val
        expr = str(new_val)
    
    return expr

for line in sys.stdin:
    if not line.strip():  # Skip empty lines
        continue
    try:
        result = evaluate_expression(line.strip())
        print("{:.2f}".format(float(result)))
    except Exception as e:
        print("Error evaluating expression", e)
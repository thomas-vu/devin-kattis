def evaluate_expression(expression):
    # Replace all '<]:=' with '0' in the expression
    expression = expression.replace('1<]:=', '1').replace('<]:=','0')
    
    # Evaluate the expression using eval to handle standard order of operations
    result = eval(expression)
    
    # Replace all '0' with '<]:=' in the result before returning
    return str(result).replace('0', '1<]:=')

# Read input from stdin
n = int(input().strip())
expression = input().strip()

# Output the evaluated expression
print(evaluate_expression(expression))
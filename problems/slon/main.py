import re
from sympy import symbols, parse_expr

def evaluate_expression(x_value, expr):
    x = symbols('x')
    parsed_expr = parse_expr(expr.replace('x', f'{x_value}'))
    return int(parsed_expr.evalf()) % M

def find_minimal_x(A, P, M):
    x = symbols('x')
    expr = parse_expr(A.replace('x', f'({x})'))
    
    # Check if the expression is a polynomial of the first degree in x
    if expr.has(x):
        # Find the coefficient of x and the constant term
        coeff_x = expr.coeff(x)
        const_term = expr - coeff_x * x
        
        # Solve the equation (coeff_x * x + const_term) % M == P
        for i in range(M):
            if (coeff_x * i + const_term) % M == P:
                return i
    else:
        # If x is not present in the expression, evaluate it directly
        evaluated_expr = int(eval(A.replace('x', f'{0}'))) % M
        if evaluated_expr == P:
            return 0
    
    # If no solution is found, raise an error (though the problem guarantees a solution)
    raise ValueError("No solution found")

# Read input
A = input().strip()
P, M = map(int, input().split())

# Find and print the minimal non-negative value of x
print(find_minimal_x(A, P, M))
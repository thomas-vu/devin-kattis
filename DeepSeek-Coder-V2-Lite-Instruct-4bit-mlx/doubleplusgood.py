import re
from itertools import product

def evaluate_expression(expr):
    # Generate all possible ways to insert '+' and '*' into the expression
    plus_positions = [i for i in range(1, len(expr), 2)]
    plus_combinations = product([True, False], repeat=len(plus_positions))
    
    results = set()
    for combo in plus_combinations:
        expr_copy = list(expr)
        for i, use_plus in enumerate(combo):
            if use_plus:
                expr_copy[plus_positions[i] - (2 * i)] = '+'
        
        # Evaluate the resulting expression
        try:
            result = eval(''.join(expr_copy))
            results.add(result)
        except:
            pass
    
    return len(results)

# Read input from stdin
expr = input().strip()

# Evaluate the expression and output the number of distinct results
print(evaluate_expression(expr))
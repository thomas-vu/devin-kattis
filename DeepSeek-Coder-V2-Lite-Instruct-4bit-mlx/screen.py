import re

def evaluate_formula(R, C, formula):
    # Helper function to parse and evaluate the SIMPLE part
    def eval_simple(s):
        tokens = s.split()
        value = int(tokens[0])
        i = 1
        while i < len(tokens):
            if tokens[i] == '*':
                value *= int(tokens[i + 1])
                i += 2
            else:
                value += int(tokens[i + 1]) if tokens[i] == '+' else -int(tokens[i + 1])
                i += 2
        return value
    
    # Helper function to parse and evaluate the TERM part
    def eval_term(t):
        if '*' in t:
            parts = t.split('*')
            left = eval_term(parts[0])
            right = int(parts[1]) if len(parts) > 1 else 1
            return left * right
        else:
            return eval_simple(t)
    
    # Helper function to parse and evaluate the COMPLEX part (SQRT or FRACTION)
    def eval_complex(c):
        if '/' in c:
            parts = c.split('/')
            top = eval_term(parts[0])
            bottom = int(parts[1]) if len(parts) > 1 else 1
            return top / bottom
        elif 'sqrt' in c:
            parts = c.split('sqrt')
            inner_term = eval_term(parts[1])
            return int(inner_term ** 0.5)
        else:
            return eval_term(c)
    
    # Helper function to parse and evaluate the FORMULA part
    def eval_formula(f):
        f = f.replace(' ', '')
        if '+' in f:
            parts = f.split('+')
            left = eval_formula(parts[0])
            right = eval_formula(parts[1])
            return left + right
        elif '-' in f:
            parts = f.split('-')
            left = eval_formula(parts[0])
            right = int(parts[1]) if len(parts) > 1 else -0
            return left - right
        else:
            return eval_complex(f)
    
    # Main evaluation logic
    formula = [line.strip() for line in formula]
    if R == 1:
        simple = eval_simple(formula[0])
        return simple
    elif R == 2:
        sqrt_part = eval_complex(formula[0])
        return int(sqrt_part ** 2)
    else:
        term1 = eval_term(formula[0])
        fraction_part = eval_complex(formula[1])
        term2 = eval_term(formula[2])
        return (term1 * fraction_part - term2) / 3

# Read input and process each test case
import sys
input = sys.stdin.read
data = input().split()
T = int(data[0])
index = 1
for _ in range(T):
    R, C = int(data[index]), int(data[index + 1])
    index += 2
    formula = [data[i] for i in range(index, index + R)]
    index += R
    print(evaluate_formula(R, C, formula))
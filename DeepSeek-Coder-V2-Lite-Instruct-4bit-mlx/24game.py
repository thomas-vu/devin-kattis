from itertools import permutations, product

def evaluate(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': 
        if b != 0 and a % b == 0: return int(a / b)
        else: return float('inf')  # Division by zero or non-integer result is not allowed

def solve(cards, target):
    for a, b, c, d in permutations(cards):
        ops = ['+', '-', '*', '/']
        for op1, op2, op3 in product(ops, repeat=3):
            expr = f"(({a} {op1} {b}) {op2} {c}) {op3} {d}"
            try:
                if evaluate(evaluate(evaluate(a, b, op1), c, op2), d, op3) == target:
                    return expr
            except ZeroDivisionError:
                continue
            except ValueError:  # Invalid expression due to division by zero
                continue
    return None

# Read input
C, T = map(int, input().split())
cards = list(map(int, input().split()))

# Solve the problem and print the solution
solution = solve(cards, T)
print(solution)
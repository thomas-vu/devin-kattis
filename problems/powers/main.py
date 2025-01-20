def evaluate_expression(a, b):
    total = 0
    for i in range(1, a + 1):
        total += i ** b
    return total % a

# Read input from stdin
a, b = map(int, input().split())
print(evaluate_expression(a, b))
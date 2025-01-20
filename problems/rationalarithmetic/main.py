def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplified_fraction(numerator, denominator):
    if numerator == 0:
        return (0, 1)
    sign = -1 if numerator * denominator < 0 else 1
    numerator, denominator = abs(numerator), abs(denominator)
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    return (sign * numerator, denominator)

def perform_operation(x1, y1, op, x2, y2):
    if op == '+':
        numerator = x1 * y2 + x2 * y1
        denominator = y1 * y2
    elif op == '-':
        numerator = x1 * y2 - x2 * y1
        denominator = y1 * y2
    elif op == '*':
        numerator = x1 * x2
        denominator = y1 * y2
    elif op == '/':
        numerator = x1 * y2
        denominator = y1 * x2
    else:
        raise ValueError("Invalid operator")
    
    simplified_num, simplified_den = simplified_fraction(numerator, denominator)
    return f"{simplified_num}/{simplified_den}"

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
operations = data[1:]

results = []
for i in range(n):
    x1, y1, op, x2, y2 = int(operations[i*5]), int(operations[i*5+1]), operations[i*5+2], int(operations[i*5+3]), int(operations[i*5+4])
    result = perform_operation(x1, y1, op, x2, y2)
    results.append(result)

for result in results:
    print(result)
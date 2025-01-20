import math

def find_n(factorial):
    n = 0
    while math.prod([i for i in range(1, n + 1)]) != factorial:
        n += 1
    return n

# Read input from standard input
factorial = int(input())
n = find_n(factorial)
print(n)
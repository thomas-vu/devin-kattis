def f(x):
    if x <= 9:
        return factorial(x)
    else:
        return factorial(x % 10) + f(x // 10)

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def find_x(y):
    x = 0
    while f(x) != y:
        x += 1
    return x

# Read input from stdin
import sys
input_value = int(sys.stdin.readline().strip())

# Output the result
print(find_x(input_value))
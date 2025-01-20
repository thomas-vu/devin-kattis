def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def divides_factorial(n, m):
    fact = factorial(n)
    return fact % m == 0

while True:
    try:
        n, m = map(int, input().split())
        if divides_factorial(n, m):
            print(f"{m} divides {n}!")
        else:
            print(f"{m} does not divide {n}!")
    except EOFError:
        break
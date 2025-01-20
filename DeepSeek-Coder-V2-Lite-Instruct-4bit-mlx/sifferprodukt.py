def single_digit(x):
    while x >= 10:
        digits = [int(d) for d in str(x) if d != '0']
        x = 1
        for digit in digits:
            x *= digit
    return x

# Read input from stdin
x = int(input())
result = single_digit(x)
print(result)
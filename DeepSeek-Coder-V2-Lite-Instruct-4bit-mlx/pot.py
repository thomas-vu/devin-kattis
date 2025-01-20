def calculate_x(numbers):
    x = 0
    for number in numbers:
        digits = [int(d) for d in str(number)]
        power = digits[-1]  # The last digit is the power
        base = int(''.join(map(str, digits[:-1])))  # The rest is the base
        x += base ** power
    return x

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Calculate and output the result
x = calculate_x(numbers)
print(x)
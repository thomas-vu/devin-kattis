def last_three_digits(n):
    trailing_zeroes = 0
    i = 5
    while n // i > 0:
        trailing_zeroes += n // i
        i *= 5
    factorial = 1
    for i in range(1, n + 1):
        factorial = (factorial * i) % 1000
    return f"{factorial:03d}"

n = int(input())
print(last_three_digits(n))
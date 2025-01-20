def count_digits(n):
    if n == 0 or n == 1:
        return 1
    digits = 0
    for i in range(2, n + 1):
        digits += len(str(i))
    return digits

while True:
    try:
        n = int(input())
        print(count_digits(n))
    except EOFError:
        break
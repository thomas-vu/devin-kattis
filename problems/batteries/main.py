def min_tests(n):
    tests = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n + 1) // 2
        tests += 1
    return tests + 1

while True:
    n = int(input())
    if n == 0:
        break
    print(min_tests(n))
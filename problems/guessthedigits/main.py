def find_number(m, n, p, q):
    if m == n:
        return str(p)
    
    base = 10 ** (m - n - 1)
    min_digits = []
    
    for i in range(base):
        number = int(str(i) + str(p))
        if (number * q) % (10 ** (m - n)) == int(str(i) + str(p)):
            min_digits.append(number)
    
    if len(min_digits) == 0:
        return "IMPOSSIBLE"
    else:
        min_digits.sort()
        return str(min_digits[0])

# Read input
m, n, p, q = map(int, input().split())
# Output the result
print(find_number(m, n, p, q))
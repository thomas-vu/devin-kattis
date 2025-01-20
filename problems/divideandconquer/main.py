def valid_divisibility_hack(b, d):
    # Check if there exists a positive integer m such that the (b, d, m) divisibility hack is valid
    for m in range(1, 100):  # Try different values of m up to a reasonable limit
        valid = True
        n = b
        while n > 0:
            sum_terms = 0
            for i in range(m):
                if n > 0:
                    sum_terms += (n % (b ** (m - i))) // (b ** (m - 1 - i))
                    n //= b
                else:
                    break
            if sum_terms % d != 0:
                valid = False
                break
        if valid:
            return "yes"
    return "no"

# Read input
b, d = map(int, input().split())
print(valid_divisibility_hack(b, d))
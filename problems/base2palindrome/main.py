def is_palindrome(n, base):
    s = ""
    while n > 0:
        s += str(n % base)
        n //= base
    return s == s[::-1]

def find_mth_palindrome(m, base=2):
    count = 0
    n = 0
    while count < m:
        if is_palindrome(n, base):
            count += 1
        n += 1
    return n - 1

# Read input from stdin
import sys
input_line = sys.stdin.readline().strip()
M = int(input_line)

# Output the result
print(find_mth_palindrome(M))
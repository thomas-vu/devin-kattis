def is_palindrome(n, base):
    s = ""
    while n:
        s = str(n % base) + s
        n //= base
    return s == s[::-1]

def count_palindromes(a, b, k):
    count = 0
    for i in range(a, b + 1):
        if all(is_palindrome(i, j) for j in range(2, k + 1)):
            count += 1
    return count

a, b, k = map(int, input().split())
print(count_palindromes(a, b, k))
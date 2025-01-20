def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(n):
    count = 0
    for i in range(1, n):
        if is_palindrome(str(i)) and is_palindrome(bin(i)[2:]):
            count += 1
    return count

n = int(input().strip())
print(count_palindromes(n))
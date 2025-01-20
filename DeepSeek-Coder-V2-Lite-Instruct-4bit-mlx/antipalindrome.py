def is_palindrome(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    return s == s[::-1]

def contains_palindrome(s):
    n = len(s)
    for i in range(n - 1):
        for j in range(i + 2, n + 1):
            if is_palindrome(s[i:j]):
                return True
    return False

text = input()
if is_palindrome(text) or contains_palindrome(text):
    print("Palindrome")
else:
    print("Anti-palindrome")
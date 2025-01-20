def maximal_palindrome_partitions(s):
    n = len(s)
    for k in range(n, 0, -1):
        found = False
        for i in range(n - k + 1):
            substring = s[i:i+k]
            if substring == substring[::-1]:
                found = True
                break
        if found:
            return k
    return 1

# Read input from stdin
s = input().strip()
print(maximal_palindrome_partitions(s))
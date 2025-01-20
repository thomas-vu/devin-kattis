def min_operations_to_palindrome(s):
    n = len(s)
    operations = 0
    
    for i in range(n // 2):
        left, right = s[i], s[n - i - 1]
        if left != right:
            for j in range(i + 1, n - i - 1):
                if s[j] == left:
                    operations += j - i
                    s = s[:i] + right + s[i+1:j] + left + s[j+1:]
                    break
                elif s[j] == right:
                    operations += n - i - j - 1
                    s = s[:n - i - 1] + left + s[n - i:]
                    break
    
    return operations

# Read input from standard input
s = input().strip()

# Compute and output the result
print(min_operations_to_palindrome(s))
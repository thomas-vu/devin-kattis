def longest_repeated_substring(L, s):
    def check(length):
        seen = set()
        for i in range(L - length + 1):
            substring = s[i:i+length]
            if substring in seen:
                return True
            seen.add(substring)
        return False
    
    left, right = 0, L
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid):
            left = mid
        else:
            right = mid - 1
    return left if check(left) else 0

# Read input
L = int(input())
s = input()

# Output the result
print(longest_repeated_substring(L, s))
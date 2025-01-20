def is_internally_reversibly_cyclic(s):
    n = len(s)
    
    # Helper function to check if a string is cyclic of another
    def is_cyclic(s, t):
        return any(s[i:] + s[:i] == t for i in range(len(s)))
    
    # Check every proper substring of s
    for i in range(n):
        for j in range(i + 1, n):
            t = s[i:j]
            if not is_cyclic(s, t) or not is_cyclic(s, t[::-1]):
                return 0
    return 1

# Read input from stdin
s = input().strip()
print(is_internally_reversibly_cyclic(s))
def find_sticky_keys(s, t):
    sticky_keys = []
    for i in range(len(s)):
        if s[i] != t[2*i]:
            sticky_keys.append(s[i])
    return ''.join(sorted(set(sticky_keys)))

# Read input from stdin
s = input().strip()
t = input().strip()

# Output the result
print(find_sticky_keys(s, t))
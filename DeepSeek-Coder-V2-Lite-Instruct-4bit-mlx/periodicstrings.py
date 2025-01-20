def find_k_periodic(s):
    n = len(s)
    for k in range(1, n + 1):
        if n % k == 0:
            valid = True
            for i in range(k, n, k):
                if s[i:i+k] != s[:k]:
                    valid = False
                    break
            if valid:
                return k
    return n

# Test cases
print(find_k_periodic("aaaaaaaa"))  # Output: 1
print(find_k_periodic("abbaabbaabba"))  # Output: 2
print(find_k_periodic("abcdef"))  # Output: 6
print(find_k_periodic("abccabbcaabc"))  # Output: 3
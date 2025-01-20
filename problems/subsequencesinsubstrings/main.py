def count_substrings(s, t):
    def is_subsequence(substr, t):
        i = j = 0
        while i < len(substr) and j < len(t):
            if substr[i] == t[j]:
                i += 1
            j += 1
        return i == len(substr)
    
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_subsequence(s[i:j], t):
                count += 1
    return count

# Example usage:
# s = "abcdefghijklmnopqrstuvwxyz"
# t = "a"
# print(count_substrings(s, t))  # Output: 26
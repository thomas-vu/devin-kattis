def longest_common_substring(strings):
    if not strings:
        return 0
    
    # Start with the shortest string and expand from there
    min_len = min(len(s) for s in strings)
    
    def is_common_substring(substring):
        # Check if the substring is common to all strings
        for s in strings:
            if substring not in s:
                return False
        return True
    
    # Binary search for the longest common substring
    left, right = 0, min_len
    while left <= right:
        mid = (left + right) // 2
        if is_common_substring(strings[0][:mid]):
            left = mid + 1
        else:
            right = mid - 1
    
    return left - 1

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]

# Get the result and print it
result = longest_common_substring(strings)
print(result)
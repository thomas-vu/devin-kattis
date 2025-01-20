def min_erasures(s):
    char_count = {}
    for char in s:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    distinct_chars = len(char_count)
    if distinct_chars <= 2:
        return 0
    
    min_erasures = float('inf')
    for char in char_count:
        erasures = sum(char_count.values()) - char_count[char]
        min_erasures = min(min_erasures, erasures)
    
    return min_erasures

# Read the input from stdin
s = input().strip()
print(min_erasures(s))
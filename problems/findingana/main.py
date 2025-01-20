def find_suffix(s):
    first_a = s.find('a')
    return s[first_a:]

# Read input from stdin
s = input().strip()

# Output the suffix
print(find_suffix(s))
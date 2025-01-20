def is_desiigner_word(s):
    if not s.startswith('b'):
        return "Neibb"
    count_r = 0
    i = 1
    while i < len(s) and s[i] == 'r':
        count_r += 1
        i += 1
    if count_r < 2:
        return "Neibb"
    while i < len(s) and s[i] not in 'aeiouy':
        i += 1
    if i == len(s) or s[i] not in 'aeiouy':
        return "Neibb"
    return "Jebb"

# Read input from stdin
s = input().strip()
print(is_desiigner_word(s))
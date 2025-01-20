def can_merge(s, s1, s2):
    i = j = 0
    for char in s:
        if i < len(s1) and s1[i] == char:
            i += 1
        elif j < len(s2) and s2[j] == char:
            j += 1
        else:
            return "no"
    return "yes" if i == len(s1) and j == len(s2) else "no"

# Read input
s = input().strip()
s1 = input().strip()
s2 = input().strip()

# Check if the merged string is possible
result = can_merge(s, s1, s2)
print(result)
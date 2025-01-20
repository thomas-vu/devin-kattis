def find_longest_substring(m, s):
    n = len(s)
    max_len = 0
    pos = -1
    
    for i in range(n):
        freq = {}
        for j in range(i, n):
            char = s[j]
            freq[char] = freq.get(char, 0) + 1
            if all(value >= m for value in freq.values()):
                substr_len = j - i + 1
                if substr_len > max_len:
                    max_len = substr_len
                    pos = i
                elif substr_len == max_len and i > pos:
                    pos = i
    
    if max_len == 0 and pos == -1:
        return "none"
    else:
        return f"{max_len} {pos}"

while True:
    m, s = input().split()
    m = int(m)
    if m == 0:
        break
    print(find_longest_substring(m, s))
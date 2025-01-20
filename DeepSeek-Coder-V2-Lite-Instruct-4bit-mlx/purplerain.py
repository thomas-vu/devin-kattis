def find_least_purple_rain(s):
    n = len(s)
    max_diff = -1
    best_start, best_end = 0, n
    
    for start in range(n):
        r_count = 0
        b_count = 0
        for end in range(start, n):
            if s[end] == 'R':
                r_count += 1
            else:
                b_count += 1
            diff = r_count - b_count
            if diff > max_diff or (diff == max_diff and (best_start, best_end) > (start + 1, end + 1)):
                max_diff = diff
                best_start, best_end = start + 1, end + 1
    
    return (best_start, best_end)

# Input processing
s = input().strip()
result = find_least_purple_rain(s)
print(*result)
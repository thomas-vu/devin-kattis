def max_grants(n, grants):
    from collections import Counter
    
    count = Counter(grants)
    unique_departments = list(count.keys())
    
    max_grants_accepted = 0
    
    for start in range(n):
        current_count = Counter()
        valid = True
        for end in range(start, n):
            current_count[grants[end]] += 1
            if not all(current_count[dep] == current_count.get(unique_departments[0], 0) for dep in unique_departments):
                valid = False
                break
            if valid:
                max_grants_accepted = max(max_grants_accepted, end - start + 1)
    
    return max_grants_accepted

# Read input
n = int(input())
grants = input()

# Output the result
print(max_grants(n, grants))
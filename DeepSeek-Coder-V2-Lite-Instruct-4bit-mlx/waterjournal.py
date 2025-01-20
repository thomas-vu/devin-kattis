def find_missing_entry(n, a, b, entries):
    total_sum = sum(entries)
    possible_values = set()
    
    for i in range(a, b+1):
        if a <= total_sum + i <= b:
            possible_values.add(i)
    
    if not possible_values:
        return -1
    else:
        return sorted(possible_values)

# Read input
n, a, b = map(int, input().split())
entries = [int(input()) for _ in range(n-1)]

# Find and print the result
result = find_missing_entry(n, a, b, entries)
if result == -1:
    print(-1)
else:
    print(" ".join(map(str, result)))
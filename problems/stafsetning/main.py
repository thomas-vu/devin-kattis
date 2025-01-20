def min_days_to_fix_typos(n, m, k, typos):
    total_typos = sum(typos)
    if total_typos == 0:
        return 0
    
    days = (total_typos + k - 1) // k
    return days if days * m >= total_typos else "Infinite"

# Read input
n, m, k = map(int, input().split())
typos = list(map(int, input().split()))

# Calculate and print the result
result = min_days_to_fix_typos(n, m, k, typos)
print(result)
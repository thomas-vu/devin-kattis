def find_max_fixed(n, perm):
    max_fixed = 0
    best_k = 0
    
    for k in range(n):
        fixed_count = 0
        rotated_perm = perm[k:] + perm[:k]
        
        for i in range(n):
            if rotated_perm[i] == i + 1:
                fixed_count += 1
        
        if fixed_count > max_fixed:
            max_fixed = fixed_count
            best_k = k
        elif fixed_count == max_fixed and k < best_k:
            best_k = k
    
    return best_k, max_fixed

# Read input
n = int(input().strip())
perm = list(map(int, input().strip().split()))

# Process and output the result
k, f = find_max_fixed(n, perm)
print(k, f)
def find_smallest_integer(N, k):
    if N % 2 == 1 and k % 2 == 0:
        return (N // 2 + 1) * 2
    if k == 1:
        return N + 1
    
    min_cost = float('inf')
    min_number = float('inf')
    
    for i in range(60):
        if (N + 2**i) % 2 == k % 2 and sum([(N + 2**i) & (1 << j) for j in range(60)]) == k:
            cost = sum([2**j for j in range((N + 2**i).bit_length())])
            if cost < min_cost:
                min_cost = cost
                min_number = N + 2**i
    
    return min_number

# Read input from stdin
N, k = map(int, input().split())
print(find_smallest_integer(N, k))
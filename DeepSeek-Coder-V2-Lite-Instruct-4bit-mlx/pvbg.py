def find_wave(N, R):
    low = 1
    high = max(R) + 1
    
    while low < high:
        mid = (low + high) // 2
        total_bad_guys = sum(min(t, pi) for t in range(1, mid + 1) for pi in R)
        
        if total_bad_guys >= N * mid:
            high = mid
        else:
            low = mid + 1
    
    return low

# Read input
N = int(input())
R = list(map(int, input().split()))

# Output the result
print(find_wave(N, R))
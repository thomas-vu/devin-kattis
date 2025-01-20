def min_max_after_removal(N, K, A):
    from collections import Counter
    
    count = Counter(A)
    freqs = list(count.values())
    max_freq = max(freqs)
    
    # Binary search to find the minimum possible maximum occurrence after removal of K elements
    left, right = 1, max_freq
    
    while left < right:
        mid = (left + right) // 2
        
        # Calculate the number of elements to remove to achieve mid as the maximum frequency
        total_removals = 0
        for f in freqs:
            if f > mid:
                total_removals += f - mid
        
        # If the number of removals is more than K, we need to increase the lower bound
        if total_removals > K:
            left = mid + 1
        else:
            right = mid
    
    return left

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Get the result and print it
result = min_max_after_removal(N, K, A)
print(result)
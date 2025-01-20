def min_max_weight(n, k, weights):
    low = max(weights)
    high = sum(weights)
    
    def can_partition(max_weight):
        current_sum = 0
        box_count = 1
        for weight in weights:
            if current_sum + weight <= max_weight:
                current_sum += weight
            else:
                box_count += 1
                if box_count > k:
                    return False
                current_sum = weight
        return True
    
    while low < high:
        mid = (low + high) // 2
        if can_partition(mid):
            high = mid
        else:
            low = mid + 1
    return low

# Read input
n, k = map(int, input().split())
weights = list(map(int, input().split()))

# Output the minimum possible weight of the heaviest box
print(min_max_weight(n, k, weights))
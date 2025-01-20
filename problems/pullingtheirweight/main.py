def find_target_weight(weights):
    total_weight = sum(weights)
    min_t = float('inf')
    
    for t in range(1, 20001):
        left_sum = 0
        right_sum = 0
        equal_count = 0
        
        for weight in weights:
            if weight < t:
                left_sum += weight
            elif weight > t:
                right_sum += weight
            else:
                equal_count += 1
        
        if (total_weight - left_sum) == right_sum:
            if equal_count % 2 == 0:
                min_t = min(min_t, t)
            else:
                left_sum += (equal_count // 2) * t
                right_sum += (equal_count - equal_count // 2) * t
                if left_sum == right_sum:
                    min_t = min(min_t, t)
    
    return min_t

m = int(input())
weights = [int(input()) for _ in range(m)]
print(find_target_weight(weights))
def find_highest_k(N, T, scores):
    # Count the number of students who need at least 90% (A-), 80% (B-), and 70% (C-)
    count_90 = sum(1 for score in scores if (score / T) * 100 >= 90)
    count_80 = sum(1 for score in scores if (score / T) * 100 >= 80)
    count_70 = sum(1 for score in scores if (score / T) * 100 >= 70)
    
    # Check if the conditions are met
    if count_90 < N // 4 or count_80 < N // 2 or count_70 < (3 * N) // 4:
        return -1
    
    # Binary search to find the highest K
    left, right = 1, T
    while left < right:
        mid = (left + right) // 2
        count_90 = sum(1 for score in scores if (score / mid) * 100 >= 90)
        count_80 = sum(1 for score in scores if (score / mid) * 100 >= 80)
        count_70 = sum(1 for score in scores if (score / mid) * 100 >= 70)
        
        if count_90 < N // 4 or count_80 < N // 2 or count_70 < (3 * N) // 4:
            right = mid - 1
        else:
            left = mid + 1
    
    return right

# Read input
N, T = map(int, input().split())
scores = [int(input()) for _ in range(N)]

# Output the result
print(find_highest_k(N, T, scores))
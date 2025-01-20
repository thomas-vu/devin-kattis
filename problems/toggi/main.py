import math

def max_digits_of_pi(C):
    left, right = 0, C * 10**6
    
    while left < right:
        mid = (left + right) // 2
        time_taken = mid * math.log10(mid) / (10**6)
        
        if time_taken <= C:
            left = mid + 1
        else:
            right = mid
    
    return int(left - 1)

# Read input
C = int(input().strip())

# Calculate and output the result
print(max_digits_of_pi(C))
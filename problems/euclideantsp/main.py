import math

def find_optimal_c(n, p, s, v):
    low = 0.0
    high = 100.0
    
    while high - low > 1e-9:
        mid = (low + high) / 2
        time_for_algorithm = n * math.log2(n) ** (mid * math.sqrt(2)) / (p * 10**9)
        time_for_distribution = s * (1 + 1 / mid) / v
        if time_for_algorithm > time_for_distribution:
            high = mid
        else:
            low = mid
    
    return (low, n * math.log2(n) ** (low * math.sqrt(2)) / (p * 10**9))

# Read input
n, p, s, v = map(float, input().split())

# Calculate the optimal parameter c and total time
c, t = find_optimal_c(int(n), p, s, v)

# Output the result with the required precision
print("{:.9f} {:.9f}".format(t, c))
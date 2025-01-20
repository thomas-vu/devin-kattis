import math

def max_pickles(s, r, n, z):
    max_area = math.pi * s**2
    allowed_pickle_area = (z / 100) * max_area
    pickle_radius = r
    
    def can_fit(pickle_count):
        if pickle_count == 0:
            return True
        angle = 2 * math.asin(pickle_radius / (s - pickle_radius))
        total_area = pickle_count * math.pi * pickle_radius**2 * (angle / (2 * math.pi))
        return total_area <= allowed_pickle_area
    
    low, high = 0, n
    while low < high:
        mid = (low + high + 1) // 2
        if can_fit(mid):
            low = mid
        else:
            high = mid - 1
    
    return low

# Read input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Calculate and output the result
print(max_pickles(s, r, n, z))
def min_dyson_units(n, stars):
    from itertools import product
    
    # Helper function to check if a square is inside the Dyson Circle
    def is_inside(x, y, radius):
        return x**2 + y**2 <= radius**2
    
    # Binary search to find the minimum radius needed to enclose all stars
    def binary_search(low, high):
        while low < high:
            mid = (low + high) // 2
            if can_enclose(mid):
                high = mid
            else:
                low = mid + 1
        return low
    
    # Check if a given radius can enclose all stars
    def can_enclose(radius):
        min_x = -radius
        max_x = radius
        min_y = -radius
        max_y = radius
        
        for star in stars:
            x, y = star
            if not is_inside(x, y, radius):
                min_x = max(min_x, x - radius)
                max_x = min(max_x, x + radius)
                min_y = max(min_y, y - radius)
                max_y = min(max_y, y + radius)
        
        # Check if the bounding box can be enclosed within a square of side 2*radius
        return min_x <= -radius and max_x >= radius and min_y <= -radius and max_y >= radius
    
    # The minimum radius needed to enclose all stars is the answer
    min_radius = binary_search(0, 200001)
    
    # The number of Dyson units is the square of the minimum radius
    return min_radius**2

# Read input
n = int(input().strip())
stars = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Output the result
print(min_dyson_units(n, stars))
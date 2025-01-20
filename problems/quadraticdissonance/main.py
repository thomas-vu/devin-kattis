def find_minimum(A, B, C, D):
    # Define the function h(x) = max(f(x), g(x))
    def h(x):
        return max(x**2 + A*x + B, x**2 + C*x + D)
    
    # Find the points where f(x) and g(x) intersect
    def find_intersection(A, B, C, D):
        # The functions f(x) and g(x) intersect where x^2 + Ax + B = x^2 + Cx + D
        # This simplifies to (A - C)x = (D - B)
        if A != C:
            return (B - D) / (A - C)
        else:
            # If A == C, the functions are identical or parallel lines
            return float('inf')  # This means there's no unique intersection point
    
    x_intersection = find_intersection(A, B, C, D)
    
    # If the functions do not intersect, find the minimum of h(x) on both sides
    if x_intersection == float('inf'):
        # Find the minimum of h(x) on both sides
        x_left = find_minimum_of_quadratic(A, B, C, D, -100)
        x_right = find_minimum_of_quadratic(A, B, C, D, 100)
        h_left = h(x_left)
        h_right = h(x_right)
        if h_left < h_right:
            return x_left, h_left
        else:
            return x_right, h_right
    else:
        # Find the minimum of h(x) at the intersection point and its neighbors
        x_min = min([x_intersection, find_minimum_of_quadratic(A, B, C, D, x_intersection - 1), find_minimum_of_quadratic(A, B, C, D, x_intersection + 1)])
        return x_min, h(x_min)

def find_minimum_of_quadratic(A, B, C, D, x):
    # Find the minimum of a quadratic function f(x) = ax^2 + bx + c
    # The minimum is at x = -b/2a
    a = 1 if A == C else (A - C) / abs(A - C)
    b = (C - A) if A != C else 2 * (A if A < C else C)
    c = D - B if D != B else (B if B < D else D)
    return -b / (2 * a)

# Read input and process each case
while True:
    try:
        A, B, C, D = map(int, input().split())
        x_min, h_min = find_minimum(A, B, C, D)
        print("{:.4f} {:.4f}".format(x_min, h_min))
    except EOFError:
        break
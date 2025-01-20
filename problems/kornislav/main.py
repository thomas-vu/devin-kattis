def largest_rectangle(A, B, C, D):
    # Possible permutations of the steps taken by Kornislav's walk
    perms = [(A, B, C, D), (A, B, D, C), (A, C, B, D), (A, C, D, B),
             (A, D, B, C), (A, D, C, B), (B, A, C, D), (B, A, D, C),
             (B, C, A, D), (B, C, D, A), (B, D, A, C), (B, D, C, A),
             (C, A, B, D), (C, A, D, B), (C, B, A, D), (C, B, D, A),
             (C, D, A, B), (C, D, B, A), (D, A, B, C), (D, A, C, B),
             (D, B, A, C), (D, B, C, A), (D, C, A, B), (D, C, B, A)]
    
    max_area = 0
    for perm in perms:
        # Check all possible rectangles that can be formed with this permutation
        a, b, c, d = perm
        # Check for vertical rectangle (a + c) x (b + d)
        area = (max(a + c, b + d)) * (min(a + c, b + d))
        max_area = max(max_area, area)
        # Check for horizontal rectangle (a + b) x (c + d)
        area = (max(a + b, c + d)) * (min(a + b, c + d))
        max_area = max(max_area, area)
    
    return max_area

# Read input from stdin
A, B, C, D = map(int, input().split())
print(largest_rectangle(A, B, C, D))
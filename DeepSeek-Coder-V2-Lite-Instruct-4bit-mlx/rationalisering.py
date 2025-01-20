import math

def find_ratios(C, F):
    A = int(round((C * 10**6) / (F * 10**6)))
    B = int(round((10**6) / (F * 10**6)))
    min_diff = float('inf')
    best_A, best_B = 0, 0
    
    for b in range(1, B + 1):
        a = int(round(C * b / F))
        diff = abs((C - F) - (a / b)) + abs((C + F) - (a / b))
        if diff < min_diff:
            min_diff = diff
            best_A, best_B = a, b
        elif diff == min_diff and a * best_B < best_A * b:
            best_A, best_B = a, b
    
    return best_A, best_B

# Read input
C, F = map(float, input().split())

# Find and print the result
A, B = find_ratios(C, F)
print(A)
print(B)
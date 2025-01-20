def max_happiness(n, a):
    if n == 1:
        return 0
    
    max_happiness = float('-inf')
    
    for i in range(n):
        current_happiness = 0
        for j in range(n):
            position = (j + 1) % n if i == j else (j + 1)
            current_happiness += position * a[j]
        max_happiness = max(max_happiness, current_happiness)
    
    return max_happiness

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(max_happiness(n, a))
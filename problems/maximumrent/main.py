def max_rent(a, b, m, sigma):
    max_R = 0
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            if x + y <= m and 2 * x + y >= sigma:
                R = a * x + b * y
                if R > max_R:
                    max_R = R
    return max_R

# Read input
a, b = map(int, input().split())
m, sigma = map(int, input().split())

# Calculate and print the result
print(max_rent(a, b, m, sigma))
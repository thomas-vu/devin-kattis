import math

def price(p, a, b, c, d, k):
    return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)

def max_decline(p, a, b, c, d, n):
    prices = [price(p, a, b, c, d, k) for k in range(1, n + 1)]
    max_decline = 0.0
    min_price = float('inf')
    
    for i in range(n - 1):
        min_price = min(min_price, prices[i])
        max_decline = max(max_decline, prices[i] - min_price)
    
    return max_decline

# Read input
p, a, b, c, d, n = map(int, input().split())

# Calculate and output the result
result = max_decline(p, a, b, c, d, n)
print("{:.8f}".format(result))
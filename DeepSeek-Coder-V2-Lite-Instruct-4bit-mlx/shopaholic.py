def maximum_discount(n, prices):
    prices.sort(reverse=True)
    total_discount = 0
    
    for i in range(2, n, 3):
        total_discount += prices[i]
    
    return total_discount

# Read input from stdin
n = int(input().strip())
prices = list(map(int, input().strip().split()))

# Calculate and print the maximum discount
print(maximum_discount(n, prices))
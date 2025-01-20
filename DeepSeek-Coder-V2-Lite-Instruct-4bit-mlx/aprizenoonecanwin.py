def max_items(n, X, prices):
    prices.sort()
    left = 0
    right = n - 1
    count = 0
    
    while left < right:
        if prices[left] + prices[right] > X:
            count += 1
            left += 1
            right -= 1
        else:
            break
    
    return count

# Read input
n, X = map(int, input().split())
prices = list(map(int, input().split()))

# Get the result and print it
result = max_items(n, X, prices)
print(result)
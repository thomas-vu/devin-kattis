def can_buy(N, P, K, prices, categories):
    category_prices = {}
    for i in range(N):
        cat = categories[i]
        price = prices[i]
        if cat not in category_prices:
            category_prices[cat] = []
        category_prices[cat].append(price)
    
    total_cost = 0
    count = 0
    for cat, prices in category_prices.items():
        prices.sort()
        max_purchases = min(K, len(prices))
        for i in range(max_purchases):
            if total_cost + prices[i] <= P:
                total_cost += prices[i]
                count += 1
    return count

# Read input
N = int(input())
P = int(input())
K = int(input())
prices = list(map(int, input().split()))
categories = list(map(int, input().split()))

# Calculate and print the result
result = can_buy(N, P, K, prices, categories)
print(result)
def min_total_price(N, prices):
    prices.sort()
    total_cost = 0
    i = N - 1
    while i >= 0:
        if i == 0:
            total_cost += prices[i]
            break
        elif i == 1:
            total_cost += prices[i] + prices[i - 1]
            break
        elif i == 2:
            total_cost += prices[i] + prices[i - 1] + prices[i - 2]
            break
        else:
            total_cost += min(prices[i] + prices[i - 1], prices[i] + prices[i - 2])
            i -= 3
    return total_cost

N = int(input())
prices = [int(input()) for _ in range(N)]
print(min_total_price(N, prices))
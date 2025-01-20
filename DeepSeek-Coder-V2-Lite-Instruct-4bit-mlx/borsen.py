n = int(input())
fee = float(input()) / 100
prices = [float(input()) for _ in range(n)]

cash = 100.0
stocks = 0

for i in range(n):
    if i < n - 1:
        # Buy as much stock as possible today and tomorrow will be more expensive
        if prices[i] < prices[i + 1]:
            buy_amount = min(int((cash / prices[i]) - fee), int((100 / (prices[i] * (1 + fee))) * cash))
            if buy_amount > 0:
                cash -= buy_amount * prices[i] + fee
                stocks += buy_amount
    
    # Sell all stock today if tomorrow will be cheaper or equal in price
    if i < n - 1 and prices[i] >= prices[i + 1]:
        sell_amount = stocks
        cash += sell_amount * prices[i] - fee
        stocks = 0

# Sell the last stock if there is any left
if stocks > 0:
    cash += stocks * prices[-1] - fee

print("{:.10f}".format(cash))
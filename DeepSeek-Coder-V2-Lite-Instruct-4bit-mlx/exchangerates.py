def max_money(prices, days):
    n = len(prices)
    dp = [[0 for _ in range(n + 1)] for _ in range(2)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            dp[j % 2][i] = max(dp[(j + 1) % 2][i + 1], (prices[i] * dp[(j + 1) % 2][i]) / 0.97)
    
    return dp[0][0]

def main():
    while True:
        days = int(input())
        if days == 0:
            break
        
        prices = []
        for _ in range(days):
            price = float(input())
            prices.append(price)
        
        result = max_money(prices, days)
        print("{:.2f}".format(result))

if __name__ == "__main__":
    main()
def calculate_profit(N, T, K, cards, prices):
    buy_prices = [0] * (T + 1)
    sell_prices = [0] * (T + 1)
    
    for i in range(len(prices)):
        a_i, b_i = prices[i]
        buy_prices[i + 1] = a_i
        sell_prices[i + 1] = b_i
    
    min_profit = float('inf')
    
    for combo in range(1, K + 1):
        profit = 0
        extra_combos = combo - cards.count(combo)
        
        for i in range(1, T + 1):
            if cards.count(i) > combo:
                profit += (cards.count(i) - combo) * sell_prices[i]
            elif extra_combos > 0 and cards.count(i) < combo:
                profit -= (combo - cards.count(i)) * buy_prices[i]
        
        min_profit = min(min_profit, profit)
    
    return min_profit

# Read input
N, T, K = map(int, input().split())
cards = list(map(int, input().split()))
prices = [list(map(int, input().split())) for _ in range(T)]

# Calculate and output the result
profit = calculate_profit(N, T, K, cards, prices)
print(-profit if profit < 0 else profit)
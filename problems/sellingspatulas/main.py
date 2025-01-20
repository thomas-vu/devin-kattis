def find_most_profitable_period(sales):
    max_profit = 0.0
    best_start = -1
    best_end = -1
    
    for start in range(1440):
        end = start + 1
        while end <= 1440:
            total_profit = sum(sale[1] for sale in sales if start < int(sale[0]) <= end)
            cost = (end - start) * 0.08
            profit = total_profit - cost
            
            if profit > max_profit:
                max_profit = profit
                best_start = start
                best_end = end
            elif profit == max_profit and (end - start) < (best_end - best_start):
                best_start = start
                best_end = end
            elif profit == max_profit and (end - start) == (best_end - best_start) and start < best_start:
                best_start = start
                best_end = end
            end += 1
    
    if max_profit > 0:
        return f"{max_profit:.2f} {best_start} {best_end}"
    else:
        return "no profit"

while True:
    n = int(input())
    if n == 0:
        break
    
    sales = [tuple(map(float, input().split())) for _ in range(n)]
    print(find_most_profitable_period(sales))
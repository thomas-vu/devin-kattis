def calculate_segments(daily_profits, min_size, max_size):
    n = len(daily_profits)
    min_profit = float('inf')
    max_profit = float('-inf')
    
    for size in range(min_size, max_size + 1):
        for start in range(n - size + 1):
            segment_profit = sum(daily_profits[start:start + size])
            min_profit = min(min_profit, segment_profit)
            max_profit = max(max_profit, segment_profit)
    
    min_count = 0
    max_count = 0
    
    for size in range(min_size, max_size + 1):
        for start in range(n - size + 1):
            segment_profit = sum(daily_profits[start:start + size])
            if segment_profit > 0:
                min_count += 1
            if segment_profit > 0:
                max_count += 1
    
    return min_count, max_count

# Read input
n, l, h = map(int, input().split())
daily_profits = [int(input()) for _ in range(n)]

# Calculate and output the result
min_profit, max_profit = calculate_segments(daily_profits, l, h)
print(min_profit, max_profit)
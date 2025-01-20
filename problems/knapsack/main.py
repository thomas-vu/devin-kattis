def knapsack(capacity, items):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for __ in range(n + 1)]
    
    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-items[i-1][1]] + items[i-1][0])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Find the solution by tracing back through the table
    w = capacity
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(i-1)
            w -= items[i-1][1]
    
    chosen_items.reverse()
    return dp[n][capacity], chosen_items

def main():
    while True:
        try:
            capacity, n = map(int, input().split())
            items = []
            for i in range(n):
                value, weight = map(int, input().split())
                items.append((value, weight))
            
            value, chosen_items = knapsack(capacity, items)
            print(len(chosen_items))
            for item in chosen_items:
                print(item, end=' ')
            print()
        except EOFError:
            break

if __name__ == "__main__":
    main()
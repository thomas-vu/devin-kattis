def min_coins(n):
    coins = [1000, 100, 10, 1]
    count = 0
    
    for coin in coins:
        while n >= coin:
            count += 1
            n -= coin
    
    return count

# Read input from stdin
n = int(input().strip())
print(min_coins(n))
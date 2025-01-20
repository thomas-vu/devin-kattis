MOD = 10**9 + 7

def min_loot(k, coins):
    total = sum([coins[i] * (1 << i) for i in range(k)])
    half = total // 2
    
    loot_taken = 0
    for i in range(k):
        if coins[i] > 0:
            max_coins = min(coins[i], total // (2 << i))
            loot_taken += max_coins * (1 << i)
            total -= max_coins * (2 ** i)
        if loot_taken > half:
            break
    
    return (loot_taken, total)

def main():
    k = int(input())
    coins = list(map(int, input().split()))
    
    loot_taken, remaining = min_loot(k, coins)
    while remaining > 0 and loot_taken <= remaining:
        for i in reversed(range(k)):
            if coins[i] > 0 and loot_taken + (1 << i) <= remaining:
                coins[i] -= 1
                loot_taken += (1 << i)
                remaining -= (1 << i)
    
    print(remaining % MOD)

if __name__ == "__main__":
    main()
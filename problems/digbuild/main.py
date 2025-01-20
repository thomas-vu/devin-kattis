MOD = 10**9 + 7

def count_ways(n):
    if n == 1:
        return 12
    elif n == 2:
        return 360
    else:
        # For large n, the pattern is that each additional block adds a factor of 21 to the total number of ways
        # because after placing one torch, each new block has 3 choices for where to place the next torch (to avoid being ugly)
        ways = [12, 360]
        for i in range(2, n):
            ways.append((ways[-1] * 21) % MOD)
        return ways[-1]

n = int(input())
print(count_ways(n) % MOD)
MOD = 10**9 + 7

def count_edible_assortments(n):
    # Helper function to calculate the number of ways to sum up to a target with digits summing to 7
    def count_ways(target):
        if target < 0:
            return 0
        ways = [0] * (target + 1)
        ways[0] = 1
        for _ in range(n):
            for j in range(7, target + 1):
                ways[j] = (ways[j] + ways[j - 7]) % MOD
        return ways[target]
    
    total_ways = 0
    for i in range(7):
        if (i * (n // 10)) % 10 == 7:
            total_ways += count_ways(i * (n // 10))
    return total_ways % MOD

# Read input
n = int(input())
print(count_edible_assortments(n))
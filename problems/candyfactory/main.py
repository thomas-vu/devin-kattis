def min_additional_candies(n, k, candies):
    from math import gcd
    
    # Calculate the greatest common divisor of all quantities
    lcm = candies[0]
    for i in range(1, n):
        lcm = (lcm * candies[i]) // gcd(lcm, candies[i])
    
    # Calculate the total quantity of candies needed to make packs without leftovers
    total_needed = lcm * k
    
    # Calculate the sum of existing candies
    total_existing = sum(candies)
    
    # The minimum additional candies needed
    return total_needed - total_existing

# Read input
n, k = map(int, input().split())
candies = [int(input()) for _ in range(n)]

# Output the result
print(min_additional_candies(n, k, candies))
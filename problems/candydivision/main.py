import math

def find_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

N = int(input().strip())
factors = find_factors(N)
factors.remove(1)  # Remove the number of candies itself as a factor since we don't want to count Benny inviting himself
factors.remove(N)  # Remove the number of candies itself as a factor since it's not valid
factors = [x - 1 for x in factors]  # Subtract 1 from each factor to get the number of friends
factors.sort()
print(' '.join(map(str, factors)))
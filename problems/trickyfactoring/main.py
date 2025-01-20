def count_possible_b(a, c):
    def prime_factors(n):
        factors = []
        # Check for number of 2s that divide n
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        # Check for odd factors from 3 onwards
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        # If n is a prime number greater than 2
        if n > 2:
            factors.append(n)
        return factors
    
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    factors_a = prime_factors(a)
    factors_c = prime_factors(c)
    
    # Combine the prime factors of a and c
    combined_factors = list(set(factors_a + factors_c))
    
    count = 0
    for d in range(-10**6, 10**6):
        valid = True
        for factor in combined_factors:
            if d % factor == 0 and (d // factor) % a == 0:
                continue
            else:
                valid = False
                break
        if valid and (d**2) % (4*a) == 0:
            count += 1
    return count

# Read input from stdin
a, c = map(int, input().split())
print(count_possible_b(a, c))
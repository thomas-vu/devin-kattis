def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_with_substring(l, h, p):
    primes = []
    num = 2
    while len(primes) < h:
        if is_prime(num):
            primes.append(str(num))
        num += 1
    
    count = 0
    for prime in primes[l-1:h]:
        if str(p) in prime:
            count += 1
    return count

# Read input
l, h = map(int, input().split())
p = int(input())

# Convert p to string with leading zeroes if necessary
p_str = f"{p:06d}"

# Count and output the result
print(count_primes_with_substring(l, h, p_str))
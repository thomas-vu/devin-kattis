def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(a, b):
    count = 0
    for i in range(a, b + 1):
        if is_prime(i):
            count += 1
    return count

# Example usage:
# print(count_primes(1, 100))  # Output: 25
# print(count_primes(3, 5))    # Output: 2
# print(count_primes(42, 1337)) # Output: 204
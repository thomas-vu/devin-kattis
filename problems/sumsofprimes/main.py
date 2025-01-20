def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(n):
    prime_sum = 0
    for i in range(2, n):
        if is_prime(i):
            prime_sum += i
    return prime_sum

n = int(input())
print(sum_of_primes(n))
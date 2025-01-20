def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_consecutive_primes(n):
    primes = [i for i in range(2, n) if is_prime(i)]
    max_length = 0
    best_sum = 0
    
    for i in range(len(primes)):
        current_sum = 0
        for j in range(i, len(primes)):
            current_sum += primes[j]
            if current_sum >= n:
                break
            if is_prime(current_sum):
                length = j - i + 1
                if length > max_length:
                    max_length = length
                    best_sum = current_sum
                elif length == max_length:
                    best_sum = min(best_sum, current_sum)
    
    return best_sum

n = int(input().strip())
print(sum_of_consecutive_primes(n))
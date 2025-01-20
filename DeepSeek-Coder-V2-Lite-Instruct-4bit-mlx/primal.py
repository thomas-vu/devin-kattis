def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_divisor(segment):
    max_prime = 0
    for num in segment:
        if is_prime(num):
            max_prime = max(max_prime, num)
    return max_prime if max_prime > 1 else 0

def find_max_score(n, k, sequence):
    max_score = 0
    for i in range(n - k + 1):
        segment = sequence[i:i+k]
        score = prime_divisor(segment)
        max_score = max(max_score, min(score for score in segment if score > 1))
    return max_score

# Read input
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Calculate and output the maximum score
print(find_max_score(n, k, sequence))
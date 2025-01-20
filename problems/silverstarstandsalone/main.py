def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_trajectories(P):
    if not is_prime(P):
        return 0
    
    # Generate the sequence of prime numbers up to P
    primes = [2]
    num = 3
    while primes[-1] < P:
        if is_prime(num):
            primes.append(num)
        num += 2
    
    # Filter primes to be within the distance of at most 14 AU from each other
    filtered_primes = [2]  # Always include the starting prime (distance of 2 AU)
    for i in range(1, len(primes)):
        if primes[i] - primes[i-1] <= 14:
            filtered_primes.append(primes[i])
    
    # Include Silver Star (P) at the end
    if P - filtered_primes[-1] <= 14:
        filtered_primes.append(P)
    
    # Calculate the number of different trajectories
    n = len(filtered_primes)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = sum(dp[j] for j in range(max(0, i - 15), i - 1))
    
    return dp[n]

# Read input from console
P = int(input().strip())
print(count_trajectories(P))
def generate_numbers(primes, X, Y):
    def is_valid(num):
        for prime in primes:
            if num % prime == 0:
                return False
        return True
    
    valid_numbers = set()
    for i in range(X, Y + 1):
        if is_valid(i):
            valid_numbers.add(i)
    
    if not valid_numbers:
        return "none"
    else:
        return ",".join(map(str, sorted(valid_numbers)))

while True:
    N = int(input())
    if N == 0:
        break
    
    primes = list(map(int, input().split()))
    X, Y = map(int, input().split())
    
    result = generate_numbers(primes, X, Y)
    print(result)
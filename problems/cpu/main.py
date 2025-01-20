def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_explosive_numbers(A, B):
    primes = [i for i in range(2, 10**6) if is_prime(i)]
    explosive_numbers = set()
    
    for p0 in primes:
        if p0 % A == 1:
            product = p0
            sequence = [p0]
            while len(sequence) < 3 or (len(sequence) > 2 and sequence[-1] % A == 1):
                next_prime = product + B
                if is_prime(next_prime) and next_prime not in sequence:
                    sequence.append(next_prime)
                    product = next_prime
                else:
                    break
            if len(sequence) >= 3 and sequence[-1] % A == 1:
                explosive_numbers.add(product)
    return len(explosive_numbers)

def main():
    N = int(input())
    for _ in range(N):
        L, H = map(int, input().split())
        print(generate_explosive_numbers(3, 2))

if __name__ == "__main__":
    main()
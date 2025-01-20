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

def count_primes(digits):
    from itertools import permutations
    unique_numbers = set()
    for perm in set(permutations(digits)):
        number = int(''.join(perm))
        if number not in unique_numbers and is_prime(number):
            unique_numbers.add(number)
    return len(unique_numbers)

def main():
    c = int(input())
    for _ in range(c):
        digits = input().strip()
        print(count_primes(digits))

if __name__ == "__main__":
    main()
from collections import deque

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

def generate_primes(start, end):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        number, cost = queue.popleft()
        if number == end:
            return cost
        if (number, cost) in visited:
            continue
        visited.add((number, cost))
        for i in range(4):
            for digit in map(str, range(10)):
                new_number = list(str(number))
                new_number[i] = digit
                new_number = int(''.join(new_number))
                if is_prime(new_number) and new_number not in visited:
                    queue.append((new_number, cost + 1))
    return "Impossible"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    test_cases = int(data[0])
    results = []
    for i in range(1, test_cases + 1):
        start, end = int(data[i*2-1]), int(data[i*2])
        result = generate_primes(start, end)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
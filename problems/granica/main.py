def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_common_remainder(numbers):
    min_num = min(numbers)
    max_possible_m = min_num // 2
    
    possible_ms = []
    for m in range(2, max_possible_m + 1):
        remainder = numbers[0] % m
        if all(num % m == remainder for num in numbers):
            possible_ms.append(m)
    return possible_ms

def main():
    N = int(input())
    numbers = [int(input()) for _ in range(N)]
    possible_ms = find_common_remainder(numbers)
    print(' '.join(map(str, possible_ms)))

if __name__ == "__main__":
    main()
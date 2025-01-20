import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    x, y = map(int, input().split())
    
    if y % x != 0:
        print()
        return
    
    n = y // x
    
    pairs = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a = i * x
            b = (n // i) * x
            if gcd(a, b) == x:
                pairs.append((min(a, b), max(a, b)))
    
    for pair in sorted(pairs):
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
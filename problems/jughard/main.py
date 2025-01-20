def can_measure_water(a, b, d):
    if d == 0:
        return True
    if a > b:
        a, b = b, a
    while b > 0 and d % (b // gcd(a, b)) != 0:
        a, b = b - a, a
    return d % (b // gcd(a, b)) == 0

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    T = int(input())
    for _ in range(T):
        a, b, d = map(int, input().split())
        if can_measure_water(a, b, d):
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
def lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)

def next_appearance(y, c1, c2):
    l = lcm(c1, c2)
    year = y
    while year <= 2021:
        year += l
    return year

def main():
    k = int(input())
    for _ in range(k):
        y, c1, c2 = map(int, input().split())
        print(next_appearance(y, c1, c2))

if __name__ == "__main__":
    main()
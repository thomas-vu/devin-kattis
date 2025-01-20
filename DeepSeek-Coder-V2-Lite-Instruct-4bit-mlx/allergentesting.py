import math

def min_sites(n, d):
    if n == 1:
        return math.ceil(math.log2(d + 1))
    else:
        x = math.ceil(math.log2(d + 1))
        return min(x, n)

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, d = map(int, input().split())
        results.append(min_sites(n, d))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
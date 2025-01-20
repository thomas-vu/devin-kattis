def min_area(a, b):
    if a > b:
        return a * (a // 2 + 1)
    else:
        return b * (b // 2 + 1)

def solve(a, b, c, d):
    return min_area(a + c, max(b, d)) + min_area(a + d, max(b, c))

def main():
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        print(min(solve(a, b, c, d), solve(c, d, a, b)))

main()
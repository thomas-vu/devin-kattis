def count_ways(n):
    if n == 0:
        return 1
    elif n == 2:
        return 1
    else:
        ways = [0] * (n + 1)
        ways[0], ways[2] = 1, 1
        for i in range(4, n + 1, 2):
            ways[i] = ways[i - 2] + ways[i - 4]
        return ways[n]

def main():
    P = int(input())
    for _ in range(P):
        K, S = map(int, input().split())
        ways = count_ways(S)
        print(f"{K} {ways}")

if __name__ == "__main__":
    main()
def sum_multiples(p, q, n):
    total = 0
    for i in range(1, n + 1):
        total += (p * i) % q
    return total

def main():
    W = int(input())
    results = []
    for _ in range(W):
        p, q, n = map(int, input().split())
        results.append(sum_multiples(p, q, n))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
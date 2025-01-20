def min_training_runs(n, k, a, b):
    if (a * k) >= (b * n):
        return 0
    casual_runners = k - n
    if (a * k) < (b * n):
        return 1
    else:
        return -1

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n, k, a, b = map(int, input().split())
        result = min_training_runs(n, k, a, b)
        results.append(result)
    for result in results:
        print(result)

main()
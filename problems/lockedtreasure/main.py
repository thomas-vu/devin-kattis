def min_locks(n, m):
    if n == m:
        return 1
    locks = []
    for i in range(1, n+1):
        if (n - i) >= m - 1:
            locks.append(i)
    return len(locks)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    cases = int(data[0])
    index = 1
    results = []
    for _ in range(cases):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        results.append(min_locks(n, m))
    for result in results:
        print(result)

main()
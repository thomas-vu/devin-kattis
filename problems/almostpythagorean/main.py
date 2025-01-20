def count_triples(n):
    count = 0
    for a in range(n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a**2 + b** хода для всех комбинаций a, b, c
                    count += 1
    return count

n = int(input())
print(count_triples(n))
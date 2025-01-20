def count_ways(n):
    ways = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ways += 1
            if i != n // i:
                ways += 1
    return ways

while True:
    n = int(input())
    if n == 0:
        break
    print(count_ways(n))
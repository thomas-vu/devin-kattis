n = int(input())
count = 0
for a in range(1, n):
    for b in range(a, n):
        if a**2 + b**2 < (c := ((a**2 + b**2) % n)) == 0:
            c = n
        if a**2 + b**2 >= n and c < min(a, b):
            count += 1
print(count)
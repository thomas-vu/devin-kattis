n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x, y = map(int, input().split())

# Check if it's possible to make the Stupendous Stew
possible = False
for i in range(n):
    for j in range(n):
        if abs((a[i] * (1 - b[j]) + a[j] * (1 - b[i])) / 2) <= x and abs((b[i] * (1 - a[j]) + b[j] * (1 - a[i])) / 2) <= y:
            possible = True
            break
    if possible:
        break

if not possible:
    print("No")
else:
    print("Yes")
    # Calculate the proportions of each soup used in the mixture
    p = [0] * n
    for i in range(n):
        for j in range(n):
            if (a[i] * (1 - b[j]) + a[j] * (1 - b[i])) / 2 == x and (b[i] * (1 - a[j]) + b[j] * (1 - a[i])) / 2 == y:
                p = [(1 - b[j]) / (n * 2), (1 - b[i]) / (n * 2), b[i] / n, b[j] / n]
                break
    print(" ".join(map(str, p)))
def find_s(n, a):
    s = 0
    for i in range(n - 1, -1, -1):
        s = (a[i] ^ (s + i))
    return s

# Read input
n = int(input())
a = list(map(int, input().split()))

# Output the result
print(find_s(n, a))
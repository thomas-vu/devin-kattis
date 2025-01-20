def largest_number(n, a):
    while len(a) > 1:
        merged = False
        for i in range(len(a) - 1):
            if a[i] == a[i + 1]:
                a[i] *= 2
                del a[i + 1]
                merged = True
                break
        if not merged:
            a.pop()
    return a[0]

# Read input
n = int(input().strip())
a = list(map(int, input().strip().split()))

# Output the result
print(largest_number(n, a))
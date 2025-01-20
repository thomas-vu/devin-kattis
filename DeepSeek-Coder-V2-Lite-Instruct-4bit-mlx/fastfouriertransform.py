n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Initialize the result array with zeros of size n+m-1
result = [0] * (n + m - 1)

# Perform polynomial multiplication using convolution
for i in range(n):
    for j in range(m):
        result[i + j] += a[i] * b[j]

# Print the result without trailing zeroes
print(' '.join(map(str, result)))
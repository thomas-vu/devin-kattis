# Read the number of coefficients for each polynomial
n, m = map(int, input().split())
# Read the coefficients of the first polynomial
a = list(map(int, input().split()))
# Read the coefficients of the second polynomial
b = list(map(int, input().split()))
# Initialize the result list with zeros
result = [0] * (n + m - 1)
# Perform polynomial multiplication
for i in range(n):
    for j in range(m):
        result[i + j] += a[i] * b[j]
# Print the resulting polynomial coefficients
print(' '.join(map(str, result)))
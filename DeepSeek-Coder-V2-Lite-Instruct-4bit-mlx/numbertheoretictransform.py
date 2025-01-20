# Assuming you have the necessary imports for handling large integers and polynomials
MOD = 998244353
# Fast Fourier Transform (FFT) implementation for polynomial multiplication modulo MOD
def fft(a, b, n):
    if n == 1:
        return [a[0] * b[0] % MOD]
    a1, a2 = a[:n//2], a[n//2:]
    b1, b2 = b[:n//2], b[n//2:]
    y1 = fft(a1, b1, n//2)
    y2 = fft(a2, b2, n//2)
    w_n = pow(3, (MOD-1) // n, MOD)
    w = 1
    y = [0] * n
    for k in range(n//2):
        y[k] = (y1[k] + w * y2[k]) % MOD
        y[k+n//2] = (y1[k] - w * y2[k]) % MOD
        w = w * w_n % MOD
    return y

# Read input
import sys
input = sys.stdin.read
data = input().split()
n, m = int(data[0]), int(data[1])
a = list(map(int, data[2:n+2]))
b = list(map(int, data[n+2:]))
# Perform FFT for polynomial multiplication
result = fft(a, b, n + m - 1)
# Output the result
print(' '.join(map(str, result)))
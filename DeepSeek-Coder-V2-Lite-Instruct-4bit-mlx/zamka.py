L = int(input())
D = int(input())
X = int(input())

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Find the minimal integer N
N = None
for i in range(L, D + 1):
    if sum_of_digits(i) == X:
        N = i
        break

# Find the maximal integer M
M = None
for i in range(D, L - 1, -1):
    if sum_of_digits(i) == X:
        M = i
        break

print(N)
print(M)
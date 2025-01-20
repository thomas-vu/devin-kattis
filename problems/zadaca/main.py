def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_pow(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

def last_9_digits(num):
    return num % 1000000000

# Read inputs
N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))

# Compute A and B
A = 1
B = 1
for a in A_list:
    A *= a
    A %= 1000000000
for b in B_list:
    B *= b
    B %= 1000000000

# Compute GCD of A and B
gcd_value = gcd(A, B)

# Output the last 9 digits of the GCD
print(last_9_digits(gcd_value))
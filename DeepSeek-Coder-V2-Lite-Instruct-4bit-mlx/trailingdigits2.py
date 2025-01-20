n = int(input())
modulus = 10**10
result = sum(pow(i, i, modulus) for i in range(1, n + 1)) % modulus
print(str(result)[-10:])
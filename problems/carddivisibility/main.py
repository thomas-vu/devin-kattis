L, R = map(int, input().split())
mod = 9
result = 0
for i in range(L, R + 1):
    result = (result * pow(10, len(str(i))) + i) % mod
print(result)
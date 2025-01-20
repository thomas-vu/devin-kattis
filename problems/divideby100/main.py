n, m = map(int, input().split())
result = n / m
if result < 1:
    print("0" + str(result))
else:
    print(str(result).rstrip('0'))
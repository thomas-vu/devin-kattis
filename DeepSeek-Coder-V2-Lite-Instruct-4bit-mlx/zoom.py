n, k = map(int, input().split())
x_list = list(map(int, input().split()))
result = [x_list[i*k] for i in range(n//k)]
print(*result)
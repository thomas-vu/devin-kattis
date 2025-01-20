n = int(input())
temperatures = list(map(int, input().split()))
count = sum(1 for t in temperatures if t < 0)
print(count)
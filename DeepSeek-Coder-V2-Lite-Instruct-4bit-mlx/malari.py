N, M = map(int, input().split())
painted_units = set()
for _ in range(M):
    i, j = map(int, input().split())
    painted_units.update(range(i, j + 1))
result = len(painted_units)
if result > N / 2:
    print(result)
    print("The Mexicans took our jobs! Sad!")
else:
    print(result)
    print("The Mexicans are Lazy! Sad!")
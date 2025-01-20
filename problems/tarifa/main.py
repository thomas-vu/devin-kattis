X = int(input())
N = int(input())
total_spent = 0
for _ in range(N):
    total_spent += int(input())
remaining = X - total_spent
if remaining < 0:
    remaining = 0
print(X + remaining)